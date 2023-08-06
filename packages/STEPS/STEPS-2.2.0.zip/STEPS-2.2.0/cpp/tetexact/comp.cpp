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

// STEPS headers.
#include "../common.h"
#include "../solver/compdef.hpp"
#include "comp.hpp"
#include "kproc.hpp"
#include "reac.hpp"
#include "tet.hpp"
#include "wmvol.hpp"

////////////////////////////////////////////////////////////////////////////////

NAMESPACE_ALIAS(steps::tetexact, stex);
NAMESPACE_ALIAS(steps::solver, ssolver);

////////////////////////////////////////////////////////////////////////////////

stex::Comp::Comp(steps::solver::Compdef * compdef)
: pCompdef(compdef)
, pVol(0.0)
, pTets()
{
	assert(pCompdef != 0);
}

////////////////////////////////////////////////////////////////////////////////

stex::Comp::~Comp(void)
{
}

////////////////////////////////////////////////////////////////////////////////

void stex::Comp::checkpoint(std::fstream & cp_file)
{
    // reserve
}

////////////////////////////////////////////////////////////////////////////////

void stex::Comp::restore(std::fstream & cp_file)
{
    // reserve
}

////////////////////////////////////////////////////////////////////////////////

void stex::Comp::addTet(stex::WmVol * tet)
{
	assert (tet->compdef() == def());
	pTets.push_back(tet);
	pVol += tet->vol();
}

////////////////////////////////////////////////////////////////////////////////

void stex::Comp::modCount(uint slidx, double count)
{
	assert (slidx < def()->countSpecs());
	double newcount = (def()->pools()[slidx] + count);
	assert (newcount >= 0.0);
    def()->setCount(slidx, newcount);
}

////////////////////////////////////////////////////////////////////////////////

stex::WmVol * stex::Comp::pickTetByVol(double rand01) const
{
	if (countTets() == 0) return 0;
	if (countTets() == 1) return pTets[0];

	double accum = 0.0;
	double selector = rand01 * vol();
	WmVolPVecCI t_end = endTet();
	for (WmVolPVecCI t = bgnTet(); t != t_end; ++t)
	{
		accum += (*t)->vol();
		if (selector < accum) return (*t);
	}
	assert(false);
	return 0;
}

////////////////////////////////////////////////////////////////////////////////

// END
