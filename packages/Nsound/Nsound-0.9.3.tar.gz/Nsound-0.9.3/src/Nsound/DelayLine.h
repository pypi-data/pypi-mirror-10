//-----------------------------------------------------------------------------
//
//  $Id: DelayLine.h 874 2014-09-08 02:21:29Z weegreenblobbie $
//
//  Nsound is a C++ library and Python module for audio synthesis featuring
//  dynamic digital filters. Nsound lets you easily shape waveforms and write
//  to disk or plot them. Nsound aims to be as powerful as Csound but easy to
//  use.
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
#ifndef _NSOUND_DELAY_LINE_H_
#define _NSOUND_DELAY_LINE_H_

#include <Nsound/Nsound.h>

#include <stdio.h> // for NULL definition on Mac OS X

namespace Nsound
{

///////////////////////////////////////////////////////////////////////////
class DelayLine
{
    ///////////////////////////////////////////////////////////////////////
    public:

    DelayLine(const float64 & sample_rate, const float64 & n_seconds_delay);

    virtual
    ~DelayLine();

    ///////////////////////////////////////////////////////////////////////
    float64
    read();

    ///////////////////////////////////////////////////////////////////////
    void
    write(float64 x);

    ///////////////////////////////////////////////////////////////////////
    protected:

    float64 * buffer_;
    float64 * read_ptr_;
    float64 * write_ptr_;
    float64 * last_ptr_;

    ///////////////////////////////////////////////////////////////////////
    // Disable these for now
    private:

    DelayLine(const DelayLine & copy)
        :
        buffer_(NULL),
        read_ptr_(NULL),
        write_ptr_(NULL),
        last_ptr_(NULL){};

    DelayLine & operator=(const DelayLine & rhs){return *this;};
};

}; // Nsound


#endif
