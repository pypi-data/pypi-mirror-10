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

std::vector<double> API::getBatchTetCounts(std::vector<uint> const & tets, std::string const & s) const
{
    throw steps::NotImplErr();
}

////////////////////////////////////////////////////////////////////////////////

std::vector<double> API::getBatchTriCounts(std::vector<uint> const & tris, std::string const & s) const
{
    throw steps::NotImplErr();
}

////////////////////////////////////////////////////////////////////////////////

void API::getBatchTetCountsNP(unsigned int* indices, int input_size, std::string const & s, double* counts, int output_size) const
{
    throw steps::NotImplErr();
}

////////////////////////////////////////////////////////////////////////////////

void API::getBatchTriCountsNP(unsigned int* indices, int input_size, std::string const & s, double* counts, int output_size) const
{
    throw steps::NotImplErr();
}

////////////////////////////////////////////////////////////////////////////////

// END

