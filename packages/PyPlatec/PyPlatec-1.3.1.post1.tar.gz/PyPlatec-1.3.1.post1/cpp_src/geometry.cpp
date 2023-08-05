/******************************************************************************
 *  plate-tectonics, a plate tectonics simulation library
 *  Copyright (C) 2012-2013 Lauri Viitanen
 *  Copyright (C) 2014-2015 Federico Tomassetti, Bret Curtis
 *
 *  This library is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU Lesser General Public
 *  License as published by the Free Software Foundation; either
 *  version 2.1 of the License, or (at your option) any later version.
 *
 *  This library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public
 *  License along with this library; if not, see http://www.gnu.org/licenses/
 *****************************************************************************/

#include <math.h>
#include "geometry.hpp"

//
// IntPoint
//

IntPoint::IntPoint(int x, int y)
    : _x(x), _y(y)
{ }

int IntPoint::getX() const
{
    return _x;
}

int IntPoint::getY() const
{
    return _y;
}

IntPoint operator-(const IntPoint& a, const IntPoint& b) {
    return IntPoint(a.getX() - b.getX(), a.getY() - b.getY());
}

//
// FloatPoint
//

FloatPoint::FloatPoint(float x, float y)
    : _x(x), _y(y)
{ }

float FloatPoint::getX() const
{
    return _x;
}

float FloatPoint::getY() const
{
    return _y;
}

void FloatPoint::shift(float dx, float dy, const WorldDimension& _worldDimension)
{
    _x += dx;
    _x += _x > 0 ? 0 : _worldDimension.getWidth();
    _x -= _x < _worldDimension.getWidth() ? 0 : _worldDimension.getWidth();

    _y += dy;
    _y += _y > 0 ? 0 : _worldDimension.getHeight();
    _y -= _y < _worldDimension.getHeight() ? 0 : _worldDimension.getHeight();

    p_assert(_worldDimension.contains(*this), "(FloatPoint::shift)");
}

IntPoint FloatPoint::toInt() const {
    return IntPoint((int)_x, (int)_y);
}

//
// Dimension
//

Dimension::Dimension(uint32_t width, uint32_t height) :
    _width(width), _height(height)
{
}

Dimension::Dimension(const Dimension& original) :
    _width(original.getWidth()), _height(original.getHeight())
{
}

uint32_t Dimension::getWidth() const
{
    return _width;
}

uint32_t Dimension::getHeight() const
{
    return _height;
}

uint32_t Dimension::getArea() const
{
    return _width * _height;
}

bool Dimension::contains(const uint32_t x, const uint32_t y) const
{
    return (x >= 0 && x < _width && y >= 0 && y < _height);
}

bool Dimension::contains(const float x, const float y) const
{
    return (x >= 0 && x < _width && y >= 0 && y < _height);
}

bool Dimension::contains(const FloatPoint& p) const
{
    return (p.getX() >= 0 && p.getX() < _width && p.getY() >= 0 && p.getY() < _height);
}

void Dimension::grow(uint32_t amountX, uint32_t amountY)
{
    _width += amountX;
    _height += amountY;
}

//
// WorldDimension
//

WorldDimension::WorldDimension(uint32_t width, uint32_t height) : Dimension(width, height)
{
};

WorldDimension::WorldDimension(const WorldDimension& original) : Dimension(original)
{
};

uint32_t WorldDimension::getMax() const
{
    return _width > _height ? _width : _height;
}

uint32_t WorldDimension::xMod(int x) const
{
    return (x + _width) % getWidth();
}

uint32_t WorldDimension::yMod(int y) const
{
    return (y + _height) % getHeight();
}

uint32_t WorldDimension::xMod(uint32_t x) const
{
    return (x + _width) % getWidth();
}

uint32_t WorldDimension::yMod(uint32_t y) const
{
    return (y + _height) % getHeight();
}    

void WorldDimension::normalize(uint32_t& x, uint32_t& y) const
{
    x %= _width;
    y %= _height;
}

uint32_t WorldDimension::indexOf(const uint32_t x, const uint32_t y) const
{
    return y * getWidth() + x;
}

uint32_t WorldDimension::lineIndex(const uint32_t y) const
{
    if (y<0 || y>=_height){
        throw invalid_argument("WorldDimension::line_index: y is not valid");
    }
    return indexOf(0, y);
}

uint32_t WorldDimension::yFromIndex(const uint32_t index) const
{
    return index / _width;
}

uint32_t WorldDimension::xFromIndex(const uint32_t index) const
{
    const uint32_t y = yFromIndex(index);
    return index - y * _width;
}    

uint32_t WorldDimension::normalizedIndexOf(const uint32_t x, const uint32_t y) const
{
    return indexOf(xMod(x), yMod(y));
}

uint32_t WorldDimension::xCap(const uint32_t x) const
{
    return x < _width ? x : (_width-1);
}

uint32_t WorldDimension::yCap(const uint32_t y) const
{
    return y < _height ? y : (_height-1);
}

uint32_t WorldDimension::largerSize() const
{
    return _width > _height ? _width : _height;
}


namespace Platec {

IntVector::IntVector(int x, int y)
    : _x(x), _y(y)
{ }

float IntVector::length() const {
    float nx = _x;
    float ny = _y;
    return sqrt(nx * nx + ny * ny);
}

IntVector IntVector::fromDistance(const IntPoint& a, const IntPoint& b){
    return IntVector(a.getX() - b.getX(), a.getY() - b.getY());
}

IntVector operator-(const IntVector& a, const IntVector& b) {
    return IntVector(a.x() - b.x(), a.y() - b.y());
}

FloatVector IntVector::toUnitVector() const {
    return FloatVector(_x/length(), _y/length());
}

bool operator==(const FloatVector& a, const FloatVector& b) {
    return a.x() == b.x() && a.y() == b.y();
}

FloatVector::FloatVector(float x, float y)
    : _x(x), _y(y)
{ }

IntVector FloatVector::toIntVector() const {
    return IntVector((int)_x, (int)_y);
}

FloatVector operator-(const FloatVector& a, const FloatVector& b) {
    return FloatVector(a.x() - b.x(), a.y() - b.y());
}

FloatVector operator*(const FloatVector& v, float f) {
    return FloatVector(v.x() * f, v.y() * f);
}

float FloatVector::dotProduct(const FloatVector& other) const {
    return x() * other.x() + y() * other.y();
}

float FloatVector::length() const {
    float nx = _x;
    float ny = _y;
    return sqrt(nx * nx + ny * ny);
}

}
