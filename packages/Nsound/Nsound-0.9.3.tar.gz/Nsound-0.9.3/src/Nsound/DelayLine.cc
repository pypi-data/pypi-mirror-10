//-----------------------------------------------------------------------------
//
//  $Id: DelayLine.cc 874 2014-09-08 02:21:29Z weegreenblobbie $
//
//  Copyright (c) 2007 Nick Hilton
//
//  weegreenblobbie_yahoo_com (replace '_' with '@' and '.')
//
//-----------------------------------------------------------------------------

//-----------------------------------------------------------------------------
//
//  This program is free software; you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation; either version 2 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU Library General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program; if not, write to the Free Software
//  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
//
//-----------------------------------------------------------------------------

#include <Nsound/DelayLine.h>

#include <iostream>
#include <string.h>

using namespace Nsound;

using std::cerr;
using std::endl;

//-----------------------------------------------------------------------------
DelayLine::
DelayLine(
    const float64 & sample_rate,
    const float64 & n_seconds_delay)
    :
    buffer_(NULL),
    read_ptr_(NULL),
    write_ptr_(NULL),
    last_ptr_(NULL)
{
    int32 n_samples = static_cast<int32>(sample_rate * n_seconds_delay + 0.5);

    M_ASSERT_VALUE(n_samples, >, 0);

    // Allocate raw memory to hold data in delay line

    buffer_ = new float64[n_samples];

    // Clear the memory.
    memset(buffer_, 0, sizeof(float64) * (n_samples));

    read_ptr_ = buffer_;

    write_ptr_ = buffer_ + n_samples - 1;

    last_ptr_ = buffer_ + n_samples;
}

//-----------------------------------------------------------------------------
DelayLine::
~DelayLine()
{
    delete [] buffer_;
    buffer_ = NULL;
    read_ptr_ = NULL;
    write_ptr_ = NULL;
    last_ptr_ = NULL;
}

float64
DelayLine::
read()
{
    float64 x = *read_ptr_;
    ++read_ptr_;
    if(read_ptr_ >= last_ptr_)
    {
        read_ptr_ = buffer_;
    }

    return x;
}

void
DelayLine::
write(float64 x)
{
    *write_ptr_ = x;
    ++write_ptr_;
    if(write_ptr_ >= last_ptr_)
    {
        write_ptr_ = buffer_;
    }
}

