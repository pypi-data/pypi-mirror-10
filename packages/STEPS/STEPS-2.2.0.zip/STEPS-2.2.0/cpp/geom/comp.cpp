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

// STL headers.
#include <cassert>
#include <sstream>
#include <string>

// STEPS headers.
#include "../common.h"
#include "../error.hpp"
#include "geom.hpp"
#include "comp.hpp"
#include "patch.hpp"

#include "../model/model.hpp"

////////////////////////////////////////////////////////////////////////////////

USING_NAMESPACE(std);
NAMESPACE_ALIAS(steps::wm, swm);

////////////////////////////////////////////////////////////////////////////////

swm::Comp::Comp(string const & id, swm::Geom * container, double vol)
: pID(id)
, pContainer(container)
, pVolsys()
, pVol(vol)
, pIPatches()
, pOPatches()
{
	if (pContainer == 0)
    {
        ostringstream os;
        os << "No container provided to Comp initializer function\n";
        throw steps::ArgErr(os.str());
    }

	if (pVol < 0.0)
	{
		ostringstream os;
		os << "Compartment volume can't be negative\n";
		throw steps::ArgErr(os.str());
	}
	pContainer->_handleCompAdd(this);
}

////////////////////////////////////////////////////////////////////////////////

swm::Comp::~Comp(void)
{
	if (pContainer == 0) return;
	_handleSelfDelete();
}

////////////////////////////////////////////////////////////////////////////////

void swm::Comp::setID(string const & id)
{
	assert(pContainer != 0);
	if (id == pID) return;
    // The following might raise an exception, e.g. if the new ID is not
    // valid or not unique. If this happens, we don't catch but simply let
    // it pass by into the Python layer.
    pContainer->_handleCompIDChange(pID, id);
    // This line will only be executed if the previous call didn't raise
    // an exception.
    pID = id;
}

////////////////////////////////////////////////////////////////////////////////

void swm::Comp::setVol(double vol)
{
	assert(pContainer != 0);
	if (vol < 0.0)
	{
		ostringstream os;
		os << "Compartment volume can't be negative\n";
		throw steps::ArgErr(os.str());
	}
	pVol = vol;
}

////////////////////////////////////////////////////////////////////////////////

void swm::Comp::addVolsys(std::string const & id)
{
	// string identifier is only added to set if it is not already included
	pVolsys.insert(id);
}

////////////////////////////////////////////////////////////////////////////////

void swm::Comp::delVolsys(std::string const & id)
{
	// string identifier is only removed from set if it is included
	pVolsys.erase(id);
}

////////////////////////////////////////////////////////////////////////////////

std::vector<steps::model::Spec*> swm::Comp::getAllSpecs(steps::model::Model* model)
{
    std::set<steps::model::Spec*> pSpecs;
    std::set<std::string>::iterator it;
    for (it = pVolsys.begin(); it != pVolsys.end(); it++) {
        steps::model::Volsys* volsys = model->getVolsys(*it);
        std::vector<steps::model::Spec*> specs = volsys->getAllSpecs();
        pSpecs.insert(specs.begin(), specs.end());
    }

    std::vector<steps::model::Spec*> spec_vec(pSpecs.begin(), pSpecs.end());
    return spec_vec;
}

////////////////////////////////////////////////////////////////////////////////

std::vector<steps::model::Reac*> swm::Comp::getAllReacs(steps::model::Model* model)
{
    std::set<steps::model::Reac*> pReacs;
    std::set<std::string>::iterator it;
    for (it = pVolsys.begin(); it != pVolsys.end(); it++) {
        steps::model::Volsys* volsys = model->getVolsys(*it);
        std::vector<steps::model::Reac*> reacs = volsys->getAllReacs();
        pReacs.insert(reacs.begin(), reacs.end());
    }

    std::vector<steps::model::Reac*> reac_vec(pReacs.begin(), pReacs.end());
    return reac_vec;
}

////////////////////////////////////////////////////////////////////////////////

std::vector<steps::model::Diff*> swm::Comp::getAllDiffs(steps::model::Model* model)
{
    std::set<steps::model::Diff*> pDiffs;
    std::set<std::string>::iterator it;
    for (it = pVolsys.begin(); it != pVolsys.end(); it++) {
        steps::model::Volsys* volsys = model->getVolsys(*it);
        std::vector<steps::model::Diff*> diffs = volsys->getAllDiffs();
        pDiffs.insert(diffs.begin(), diffs.end());
    }

    std::vector<steps::model::Diff*> diff_vec(pDiffs.begin(), pDiffs.end());
    return diff_vec;
}


////////////////////////////////////////////////////////////////////////////////

void swm::Comp::_addIPatch(swm::Patch * patch)
{
	assert (patch->getOComp() == this);
	// patch pointer is only added to set if it is not already included
	pIPatches.insert(patch);
}

////////////////////////////////////////////////////////////////////////////////

void swm::Comp::_delIPatch(swm::Patch * patch)
{
	assert (patch->getOComp() == this);
	pIPatches.erase(patch);
}
////////////////////////////////////////////////////////////////////////////////

void swm::Comp::_addOPatch(swm::Patch * patch)
{
	assert (patch->getIComp() == this);
	// patch pointer is only added to set if it is not already included
	pOPatches.insert(patch);
}

////////////////////////////////////////////////////////////////////////////////

void swm::Comp::_delOPatch(swm::Patch * patch)
{
	assert (patch->getIComp() == this);
	pOPatches.erase(patch);
}

////////////////////////////////////////////////////////////////////////////////

void swm::Comp::_handleSelfDelete(void)
{
	pContainer->_handleCompDel(this);
	pVol = 0.0;
	pVolsys.clear();
	pIPatches.clear();
	pOPatches.clear();
	pContainer = 0;
}

////////////////////////////////////////////////////////////////////////////////

steps::wm::Patch * swm::Comp::_getIPatch(uint lidx) const
{
	assert(lidx < pIPatches.size());
	std::set<steps::wm::Patch *>::const_iterator pit = pIPatches.begin();
	for (uint i=0; i < lidx; ++i) ++pit;
	return (*pit);
}

////////////////////////////////////////////////////////////////////////////////

steps::wm::Patch * swm::Comp::_getOPatch(uint lidx) const
{
	assert(lidx < pOPatches.size());
	std::set<steps::wm::Patch *>::const_iterator pit = pOPatches.begin();
	for (uint i=0; i < lidx; ++i) ++pit;
	return (*pit);
}

////////////////////////////////////////////////////////////////////////////////

/// END
