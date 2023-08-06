////////////////////////////////////////////////////////////////////////////////
// STEPS - STochastic Engine for Pathway Simulation
// Copyright (C) 2007-2014�Okinawa Institute of Science and Technology, Japan.
// Copyright (C) 2003-2006�University of Antwerp, Belgium.
//
// See the file AUTHORS for details.
//
// This file is part of STEPS.
//
// STEPS�is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// STEPS�is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.�If not, see <http://www.gnu.org/licenses/>.
//
////////////////////////////////////////////////////////////////////////////////

/*
 *  Last Changed Rev:  $Rev: 528 $
 *  Last Changed Date: $Date: 2014-04-16 10:42:16 +0900 (Wed, 16 Apr 2014) $
 *  Last Changed By:   $Author: wchen $
 */


// Standard library & STL headers.
#include <vector>
#include <cassert>

// STEPS headers.
#include "../common.h"
#include "kproc.hpp"

////////////////////////////////////////////////////////////////////////////////

NAMESPACE_ALIAS(steps::tetexact, stex);

////////////////////////////////////////////////////////////////////////////////

stex::KProc::KProc(void)
: rExtent(0)
, pFlags(0)
, pSchedIDX(0)
, crData()
{
}

////////////////////////////////////////////////////////////////////////////////

stex::KProc::~KProc(void)
{
}

////////////////////////////////////////////////////////////////////////////////

void stex::KProc::setActive(bool active)
{
    if (active == true) pFlags &= ~INACTIVATED;
    else pFlags |= INACTIVATED;
}

////////////////////////////////////////////////////////////////////////////////

uint stex::KProc::getExtent(void) const
{
	return rExtent;
}

////////////////////////////////////////////////////////////////////////////////

void stex::KProc::resetExtent(void)
{
	rExtent = 0;
}
////////////////////////////////////////////////////////////////////////////////

void stex::KProc::resetCcst(void) const
{
	// This should never get called on base object
	assert (false);
}

////////////////////////////////////////////////////////////////////////////////

double stex::KProc::c(void) const
{
    // Should never get called on base object
	assert (false);
}

////////////////////////////////////////////////////////////////////////////////

double stex::KProc::h(void)
{
    // Should never get called on base object
	assert (false);
}

////////////////////////////////////////////////////////////////////////////////

// END
