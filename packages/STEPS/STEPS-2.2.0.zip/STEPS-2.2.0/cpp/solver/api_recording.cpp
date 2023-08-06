////////////////////////////////////////////////////////////////////////////////
// STEPS - STochastic Engine for Pathway Simulation
// Copyright (C) 2007-2014ÊOkinawa Institute of Science and Technology, Japan.
// Copyright (C) 2003-2006ÊUniversity of Antwerp, Belgium.
//
// See the file AUTHORS for details.
//
// This file is part of STEPS.
//
// STEPSÊis free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// STEPSÊis distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.ÊIf not, see <http://www.gnu.org/licenses/>.
//
////////////////////////////////////////////////////////////////////////////////

// STL headers.
#include <string>
#include <sstream>

// STEPS headers.
#include "../common.h"
#include "../error.hpp"
#include "api.hpp"
#include "statedef.hpp"
#include "compdef.hpp"
#include "patchdef.hpp"
#include "specdef.hpp"

////////////////////////////////////////////////////////////////////////////////

USING(std, string);
USING_NAMESPACE(steps::solver);

////////////////////////////////////////////////////////////////////////////////

uint API::getNComps(void) const
{
    return pStatedef->countComps();
}

////////////////////////////////////////////////////////////////////////////////

uint API::getNPatches(void) const
{
    return pStatedef->countPatches();
}

////////////////////////////////////////////////////////////////////////////////

std::string API::getCompName(uint c_idx) const
{
    return pStatedef->compdef(c_idx)->name();
}

////////////////////////////////////////////////////////////////////////////////

std::string API::getPatchName(uint c_idx) const
{
    return pStatedef->compdef(c_idx)->name();
}

////////////////////////////////////////////////////////////////////////////////

uint API::getNCompSpecs(uint c_idx) const
{
    return pStatedef->compdef(c_idx)->countSpecs();
}

////////////////////////////////////////////////////////////////////////////////

uint API::getNPatchSpecs(uint p_idx) const
{
    return pStatedef->patchdef(p_idx)->countSpecs();
}

////////////////////////////////////////////////////////////////////////////////

std::string API::getCompSpecName(uint c_idx, uint s_idx) const
{
    return pStatedef->specdef(pStatedef->compdef(c_idx)->specL2G(s_idx))->name();
}

////////////////////////////////////////////////////////////////////////////////

std::string API::getPatchSpecName(uint p_idx, uint s_idx) const
{
    return pStatedef->specdef(pStatedef->patchdef(p_idx)->specL2G(s_idx))->name();
}

////////////////////////////////////////////////////////////////////////////////

// END

