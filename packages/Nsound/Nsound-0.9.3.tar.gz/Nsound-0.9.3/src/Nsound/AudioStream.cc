//-----------------------------------------------------------------------------
//
//  $Id: AudioStream.cc 880 2015-01-01 16:10:37Z weegreenblobbie $
//
//  Copyright (c) 2009-Present Nick Hilton
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

#include <Nsound/AudioStream.h>
#include <Nsound/Buffer.h>
#include <Nsound/Generator.h>
#include <Nsound/Nsound.h>
#include <Nsound/Plotter.h>
#include <Nsound/Sine.h>
#include <Nsound/Wavefile.h>
#include <Nsound/StreamOperators.h>

#include <iostream>
#include <limits>
#include <sstream>

using namespace Nsound;

using std::cerr;
using std::cout;
using std::endl;
using std::flush;

AudioStream::
AudioStream()
    :
    sample_rate_(44100.0),
    channels_(1),
    buffers_()
{
    M_ASSERT_VALUE(channels_, !=, 0);
    buffers_ = new Buffer[channels_];
}

AudioStream::
AudioStream(
    float64 sample_rate,
    uint32 channels,
    uint32 n_samples_pre_allocate)
    :
    sample_rate_(sample_rate),
    channels_(channels),
    buffers_(NULL)
{
    M_ASSERT_VALUE(channels_, !=, 0);

    buffers_ = new Buffer[channels_];

    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].preallocate(n_samples_pre_allocate);
    }
}

AudioStream::
AudioStream(const std::string & filename)
    :
    sample_rate_(44100.0),
    channels_(1),
    buffers_(NULL)
{
    buffers_ = new Buffer[channels_];

    // This operator is defined in Wavefile.h.
    *this <<  filename.c_str();
}


AudioStream::
AudioStream(const AudioStream & rhs)
    :
    sample_rate_(rhs.sample_rate_),
    channels_(rhs.channels_),
    buffers_(NULL)
{
    buffers_ = new Buffer[channels_];
    (*this) = rhs;
}

AudioStream::
~AudioStream()
{
    delete [] buffers_;
}

void
AudioStream::
abs()
{
    // For each channel, call the Buffer.add() methods
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].abs();
    }
}

void
AudioStream::
add(
    const AudioStream & as,
    uint32 offset,
    uint32 n_samples)
{
    // For each channel, call the Buffer.add() methods
    for(uint32 i = 0; i < as.channels_; ++i)
    {
        buffers_[i].add(as.buffers_[i], offset, n_samples);
    }
}

void
AudioStream::
add(
    const AudioStream & as,
    float64 offset_seconds,
    float64 duration_seconds)
{
    uint32 off       = static_cast<uint32>(offset_seconds   * sample_rate_);
    uint32 n_samples = static_cast<uint32>(duration_seconds * sample_rate_);

    // For each channel, call the Buffer.add() methods
    for(uint32 i = 0; i < as.channels_; ++i)
    {
        buffers_[i].add(as.buffers_[i], off, n_samples);
    }
}

void
AudioStream::
convolve(const Buffer & b)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].convolve(b);
    }
}

void
AudioStream::
dB()
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].dB();
    }
}

void
AudioStream::
derivative(uint32 n)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].derivative(n);
    }
}

const Buffer &
AudioStream::
get_at_index(uint32 i) const
{
    M_ASSERT_VALUE(i, <, channels_);
    return (*this)[i];
}

void
AudioStream::
downSample(uint32 n)
{
    for(uint32 i = 1; i < channels_; ++i)
    {
        buffers_[i].downSample(n);
    }
}

float32
AudioStream::
getDuration() const
{
    uint32 length = buffers_[0].getLength();

    for(uint32 i = 1; i < channels_; ++i)
    {
        uint32 l = buffers_[i].getLength();
        if(l < length)
        {
            length = l;
        }
    }

    return static_cast<float32>(static_cast<float64>(length) / sample_rate_);
}

uint32
AudioStream::
getLength() const
{
    uint32 length = buffers_[0].getLength();

    for(uint32 i = 1; i < channels_; ++i)
    {
        uint32 l = buffers_[i].getLength();

        if(l < length)
        {
            length = l;
        }
    }

    return length;
}

void
AudioStream::
limit(float64 min, float64 max)
{
    for(uint32 i = 1; i < channels_; ++i)
    {
        buffers_[i].limit(min, max);
    }
}

void
AudioStream::
limit(const Buffer & min, const Buffer & max)
{
    for(uint32 i = 1; i < channels_; ++i)
    {
        buffers_[i].limit(min, max);
    }
}

float64
AudioStream::
getMax() const
{
    float64 max = std::numeric_limits<float64>::min();

    for(uint32 i = 0; i < channels_; ++i)
    {
        float64 b_max = buffers_[i].getMax();
        if(b_max > max)
        {
            max = b_max;
        }
    }

    return max;
}

float64
AudioStream::
getMaxMagnitude() const
{
    float64 max = std::numeric_limits<float64>::min();

    for(uint32 i = 0; i < channels_; ++i)
    {
        float64 b_max = buffers_[i].getMaxMagnitude();
        if(b_max > max)
        {
            max = b_max;
        }
    }

    return max;
}

float64
AudioStream::
getMin() const
{
    float64 min = std::numeric_limits<float64>::max();

    for(uint32 i = 0; i < channels_; ++i)
    {
        float64 b_min = buffers_[i].getMin();
        if(b_min < min)
        {
            min = b_min;
        }
    }

    return min;
}

void
AudioStream::
mono()
{
    *this = this->getMono();
}

AudioStream
AudioStream::
getMono() const
{
    AudioStream a(sample_rate_, 1);

    a << buffers_[0];

    for(uint32 i = 1; i < channels_; ++i)
    {
        a += buffers_[i];
    }

    a /= static_cast<float64>(channels_);

    return a;
}

void
AudioStream::
normalize()
{
    float64 peak = getMaxMagnitude();

    float64 normal_factor = 1.0 / peak;

    *this *= normal_factor;
}


const Buffer &
AudioStream::
operator[](uint32 i) const
{
    M_ASSERT_VALUE(i, <, channels_);
    return buffers_[i];
}

Buffer &
AudioStream::
operator[](uint32 i)
{
    M_ASSERT_VALUE(i, <, channels_);
    return buffers_[i];
}

AudioStream &
AudioStream::
operator=(const AudioStream & rhs)
{
    if(this == &rhs) return *this;

    setNChannels(rhs.channels_);

    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] = rhs.buffers_[i];
    }

    sample_rate_ = rhs.sample_rate_;

    return *this;
}

AudioStream &
AudioStream::
operator=(const Buffer & rhs)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] = rhs;
    }

    return *this;
}

boolean
AudioStream::
operator==(const AudioStream & rhs) const
{
    if(channels_ != rhs.channels_)
    {
        return false;
    }
    else if(getLength() != rhs.getLength())
    {
        return false;
    }

    for(uint32 i = 0; i < channels_; ++i)
    {
        if(buffers_[i] != rhs.buffers_[i])
        {
            return false;
        }
    }

    return true;
}

float64
AudioStream::
operator()(uint32 channel, uint32 index) const
{
    M_ASSERT_VALUE(channel, <, channels_);
    return buffers_[channel][index];
}

AudioStreamSelection
AudioStream::
operator()(const BooleanVectorVector & bvv)
{
    AudioStreamSelection as(*this, bvv);

    return as;
}

AudioStream &
AudioStream::
operator<<(const AudioStream & rhs)
{
    // Special case.
    if(rhs.channels_ == 1 && channels_ == 2)
    {
        for(uint32 i = 0; i < 2; ++i)
        {
            buffers_[i] << rhs.buffers_[0];
        }
    }
    else
    {
        uint32 c = channels_;

        if(c > rhs.channels_) c = rhs.channels_;

        for(uint32 i = 0; i < c; ++i)
        {
            buffers_[i] << rhs.buffers_[i];
        }
    }

    return *this;
}

AudioStream &
AudioStream::
operator<<(const Buffer & rhs)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] << rhs;
    }
    return *this;
}

AudioStream &
AudioStream::
operator+=(const AudioStream & rhs)
{
    return vectorOperator(rhs,ADD);
}

AudioStream &
AudioStream::
operator+=(const Buffer & rhs)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] += rhs;
    }
    return *this;
}

AudioStream &
AudioStream::
operator-=(const AudioStream & rhs)
{
    return vectorOperator(rhs,SUBTRACT);
}

AudioStream &
AudioStream::
operator-=(const Buffer & rhs)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] -= rhs;
    }
    return *this;
}

AudioStream &
AudioStream::
operator*=(const AudioStream & rhs)
{
    return vectorOperator(rhs,MULTIPLY);
}

AudioStream &
AudioStream::
operator*=(const Buffer & rhs)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] *= rhs;
    }
    return *this;
}

AudioStream &
AudioStream::
operator/=(const Buffer & rhs)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] /= rhs;
    }
    return *this;
}

AudioStream &
AudioStream::
operator^=(const Buffer & rhs)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] ^= rhs;
    }
    return *this;
}

AudioStream &
AudioStream::
operator/=(const AudioStream & rhs)
{
    return vectorOperator(rhs,DIVIDE);
}

AudioStream &
AudioStream::
operator^=(const AudioStream & rhs)
{
    return vectorOperator(rhs, POW);
}

AudioStream &
AudioStream::
vectorOperator(const AudioStream & rhs, MathOperator op)
{
    uint32 channels_to_change = channels_;

    if(channels_ > rhs.channels_)
    {
        channels_to_change = rhs.channels_;
    }

    switch(op)
    {
        case ADD:
        {
            for(uint32 i = 0; i < channels_to_change; ++i)
            {
                buffers_[i] += rhs.buffers_[i];
            }
            break;
        }
        case SUBTRACT:
        {
            for(uint32 i = 0; i < channels_to_change; ++i)
            {
                buffers_[i] -= rhs.buffers_[i];
            }
            break;
        }
        case MULTIPLY:
        {
            for(uint32 i = 0; i < channels_to_change; ++i)
            {
                buffers_[i] *= rhs.buffers_[i];
            }
            break;
        }
        case DIVIDE:
        {
            for(uint32 i = 0; i < channels_to_change; ++i)
            {
                buffers_[i] /= rhs.buffers_[i];
            }
            break;
        }
        case POW:
        {
            for(uint32 i = 0; i < channels_to_change; ++i)
            {
                buffers_[i] ^= rhs.buffers_[i];
            }
            break;
        }
    }

    return *this;
}

AudioStream &
AudioStream::
operator<<(float64 d)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] << d;
    }
    return *this;
}

AudioStream &
AudioStream::
operator+=(float64 d)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] += d;
    }
    return *this;
}

AudioStream &
AudioStream::
operator-=(float64 d)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] -= d;
    }
    return *this;
}

AudioStream &
AudioStream::
operator*=(float64 d)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] *= d;
    }
    return *this;
}

AudioStream &
AudioStream::
operator/=(float64 d)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] /= d;
    }
    return *this;
}

AudioStream &
AudioStream::
operator^=(float64 d)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i] ^= d;
    }
    return *this;
}

std::ostream &
Nsound::
operator<<(std::ostream & out, const AudioStream & rhs)
{
    uint32 n_samples = 10;

    if(n_samples >= rhs.getLength())
    {
        n_samples = rhs.getLength();
    }

    for(uint32 i = 0; i < rhs.channels_; ++i)
    {
        out << "channel["
            << i
            << "].length = "
            << rhs.buffers_[i].getLength()
            << endl
            << "channel["
            << i
            << "] = ";

        for(uint32 j = 0; j < n_samples; j++)
        {
            out << rhs.buffers_[i][j]
                << " ";
        }
    }
    return out;
}

AudioStream
Nsound::
operator/(float64 d, const AudioStream & lhs)
{
    AudioStream temp(lhs.getSampleRate(), lhs.getNChannels());

    uint32 ch = lhs.getNChannels();

    for(uint32 i = 0; i < ch; ++i)
    {
        temp[i] = d / lhs[i];
    }

    return temp;
}

void
AudioStream::
pad(float64 fill)
{
    uint32 min = 1000000000;
    uint32 max = 0;

    for(uint32 i = 0; i < channels_; ++i)
    {
        uint32 l = buffers_[i].getLength();

        if(l < min)
        {
            min = l;
        }
        else if(l > max)
        {
            max = l;
        }
    }

    if(min != max)
    {
        for(uint32 i = 1; i < channels_; ++i)
        {
            uint32 l = buffers_[i].getLength();

            uint32 n_fill = max - l;

            if(n_fill > 0)
            {
                buffers_[i] << fill * Buffer::ones(n_fill);
            }
        }
    }
}

void
AudioStream::
pan(float64 pan)
{
    float64 left_amplitude  = (pan + 1.0) / 2.0;
    float64 right_amplitude = ((pan * -1.0) + 1.0) / 2.0;

    if(channels_ > 0)
    {
        buffers_[0] *= left_amplitude;
    }
    if(channels_ > 1)
    {
        buffers_[1] *= right_amplitude;
    }
}

void
AudioStream::
pan(const Buffer & pan)
{
    const uint32 pan_length = pan.getLength();
    const uint32 as_length = getLength();

    for(uint32 i = 0; i < as_length; ++i)
    {
        if(channels_ > 0)
        {
            float64 left_amplitude  = (pan[i % pan_length] + 1.0) / 2.0;
            buffers_[0][i] *= left_amplitude;
        }
        if(channels_ > 1)
        {
            float64 right_amplitude = ((pan[i % pan_length] * -1.0) + 1.0)
                                       / 2.0;
            buffers_[1][i] *= right_amplitude;
        }
    }
}

void
AudioStream::
plot(const std::string & title) const
{
    Plotter pylab;

    pylab.figure();

    uint32 n_rows = channels_;
    uint32 n_columns = 1;

    // Create the x axis based on seconds.
    Sine sin(sample_rate_);

    Buffer x_axis = sin.drawLine(getDuration(), 0.0, getDuration());

    // For each buffer, plot it
    for(uint32 i = 0; i < channels_; ++i)
    {
        pylab.subplot(n_rows, n_columns, i + 1);

        if(i == 0)
        {
            pylab.title(title);
        }

        pylab.plot(x_axis, buffers_[i]);

        pylab.xlabel("Time (sec)");
        pylab.ylabel("Amplitude");
    }
}

void
AudioStream::
readWavefile(const char * filename)
{
    M_CHECK_PTR(filename);

    *this << filename;
}

void
AudioStream::
resample(float64 factor)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].resample(factor);
    }
}

void
AudioStream::
resample(const Buffer & factor)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].resample(factor);
    }
}

void
AudioStream::
resample2(float64 new_sample_rate)
{
    M_ASSERT_VALUE(new_sample_rate, >, 0.0);

    float64 ratio = new_sample_rate / sample_rate_;

    resample(ratio);

    sample_rate_ = new_sample_rate;
}

void
AudioStream::
reverse()
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].reverse();
    }
}

AudioStreamSelection
AudioStream::
select(const uint32 start_index, const uint32 stop_index)
{
    BooleanVectorVector bvv;

    uint32 n_samples = getLength();

    for(uint32 i = start_index; i < stop_index; ++i)
    {
        // Create a BooleanVector of true for the length of the Buffer
        BooleanVector bv;
        bv.reserve(n_samples);
        for(uint32 j = 0; j < n_samples; ++j)
        {
            bv.push_back(true);
        }

        bvv.push_back(bv);
    }

    return AudioStreamSelection(*this, bvv);
}

void
AudioStream::
set_at_index(uint32 i, const Buffer & b)
{
    M_ASSERT_VALUE(i, <, channels_);
    (*this)[i] = b;
}

void
AudioStream::
setNChannels(uint32 channels)
{
    if(channels_ != channels)
    {
        delete [] buffers_;

        buffers_ = new Buffer [channels];

        channels_ = channels;
    }
}

void
AudioStream::
smooth(uint32 n_passes, uint32 n_samples_per_average)
{
    for(uint32 channel = 0; channel < channels_; ++channel)
    {
        buffers_[channel].smooth(n_passes, n_samples_per_average);
    }
}

void
AudioStream::
speedUp(float32 step_size)
{
    for(uint32 channel = 0; channel < channels_; ++channel)
    {
        buffers_[channel].speedUp(step_size);
    }
}

void
AudioStream::
speedUp(const Buffer & step_buffer)
{
    for(uint32 channel = 0; channel < channels_; ++channel)
    {
        buffers_[channel].speedUp(step_buffer);
    }
}

void
AudioStream::
sqrt()
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].sqrt();
    }
}

AudioStream
AudioStream::
substream(uint32 start_index, uint32 n_samples) const
{
    AudioStream new_stream(sample_rate_, channels_);

    for(uint32 channel = 0; channel < channels_; ++channel)
    {
        new_stream.buffers_[channel]
            = buffers_[channel].subbuffer(start_index, n_samples);
    }

    return new_stream;
}

AudioStream
AudioStream::
substream(float32 start_time, float32 n_seconds) const
{
    AudioStream new_stream(sample_rate_, channels_);

    uint32 start_index = static_cast<uint32>(start_time * sample_rate_);
    uint32 n_samples = static_cast<uint32>(n_seconds * sample_rate_);

    if(n_seconds == 0 || n_samples + start_index >= getLength())
    {
        n_samples = getLength() - start_index;
    }

    for(uint32 ch = 0; ch < channels_; ++ch)
    {
        new_stream.buffers_[ch] = buffers_[ch].subbuffer(start_index, n_samples);
    }

    return new_stream;
}

void
AudioStream::
transpose()
{
    // Pad with zeros if necessary.
    this->pad(0.0);

    AudioStream a(getSampleRate(), getLength());

    for(uint32 i = 0; i < getLength(); ++i)
    {
        for(uint32 j = 0; j < getNChannels(); ++j)
        {
            a[i] << (*this)[j][i];
        }
    }

    *this = a;
}

void
AudioStream::
upSample(uint32 n)
{
    for(uint32 i = 0; i < channels_; ++i)
    {
        buffers_[i].upSample(n);
    }
}

std::ostream &
AudioStream::
write(std::ostream & out) const
{
    out & 'a' & 'u' & 'd' & 'i' & 'o' & 's' & 't' & 'r'
        & getSampleRate()
        & getNChannels();

    for(uint32 i = 0; i < getNChannels(); ++i)
    {
        buffers_[i].write(out);
    }

    return out;
}

std::string
AudioStream::
write() const
{
    std::stringstream ss;
    write(ss);
    return ss.str();
}

std::istream &
AudioStream::
read(std::istream & in)
{
    char id[8];
    float64 sr = 0;
    uint32 n_channels = 0;

    in
        & id[0] & id[1] & id[2] & id[3] & id[4] & id[5] & id[6] & id[7]
        & sr & n_channels;

    if(
        id[0] != 'a' || id[1] != 'u' || id[2] != 'd' || id[3] != 'i' ||
        id[4] != 'o' || id[5] != 's' || id[6] != 't' || id[7] != 'r')
    {
        M_THROW("Did not find any Nsound AudioStream data in input stream!");
    }

    delete [] buffers_;
    buffers_ = new Buffer[n_channels];

    for(uint32 i = 0; i < n_channels; ++i)
    {
        buffers_[i].read(in);
    }

    return in;
}

void
AudioStream::
read(const std::string & in)
{
    std::stringstream ss(in);
    read(ss);
}

void
AudioStream::
writeWavefile(const char * filename) const
{
    M_CHECK_PTR(filename);

    Nsound::operator>>(*this, filename);
}


BooleanVectorVector
Nsound::
AudioStream::
operator>(float64 rhs)
{
    BooleanVectorVector bv;

    for(uint32 i = 0; i < channels_; ++i)
    {
        bv.push_back( buffers_[i] > rhs );
    }

    return bv;
}

BooleanVectorVector
Nsound::
AudioStream::
operator>=(float64 rhs)
{
    BooleanVectorVector bv;

    for(uint32 i = 0; i < channels_; ++i)
    {
        bv.push_back( buffers_[i] >= rhs );
    }

    return bv;
}

BooleanVectorVector
Nsound::
AudioStream::
operator<(float64 rhs)
{
    BooleanVectorVector bv;

    for(uint32 i = 0; i < channels_; ++i)
    {
        bv.push_back( buffers_[i] < rhs );
    }

    return bv;
}

BooleanVectorVector
Nsound::
AudioStream::
operator<=(float64 rhs)
{
    BooleanVectorVector bv;

    for(uint32 i = 0; i < channels_; ++i)
    {
        bv.push_back( buffers_[i] <= rhs );
    }

    return bv;
}

BooleanVectorVector
Nsound::
AudioStream::
operator==(float64 rhs)
{
    BooleanVectorVector bv;

    for(uint32 i = 0; i < channels_; ++i)
    {
        bv.push_back( buffers_[i] == rhs );
    }

    return bv;
}

BooleanVectorVector
Nsound::
AudioStream::
operator!=(float64 rhs)
{
    BooleanVectorVector bv;

    for(uint32 i = 0; i < channels_; ++i)
    {
        bv.push_back( buffers_[i] != rhs );
    }


    return bv;
}

AudioStream
AudioStream::
ones(
    float64 sample_rate,
    const uint32 n_channels,
    float64 duration)
{
    AudioStream a(sample_rate, n_channels);

    Generator g(sample_rate);

    a << g.drawLine(duration, 1.0, 1.0);

    return a;
}

AudioStream
AudioStream::
rand(
    float64 sample_rate,
    const uint32 n_channels,
    float64 duration)
{
    AudioStream a(sample_rate, n_channels);

    Generator g(sample_rate);

    a << g.whiteNoise(duration);

    return a;
}

AudioStream
AudioStream::
zeros(
    float64 sample_rate,
    const uint32 n_channels,
    float64 duration)
{
    AudioStream a(sample_rate, n_channels);

    Generator g(sample_rate);

    a << g.drawLine(duration, 0.0, 0.0);

    return a;
}
