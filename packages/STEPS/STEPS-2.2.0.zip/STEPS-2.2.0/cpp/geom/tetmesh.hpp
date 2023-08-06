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

/*
 *  Last Changed Rev:  $Rev: 528 $
 *  Last Changed Date: $Date: 2014-04-16 10:42:16 +0900 (Wed, 16 Apr 2014) $
 *  Last Changed By:   $Author: wchen $
 */

#ifndef STEPS_TETMESH_TETMESH_HPP
#define STEPS_TETMESH_TETMESH_HPP 1


// STEPS headers.
#include "../common.h"
#include "geom.hpp"
#include "tmpatch.hpp"
#include "tmcomp.hpp"
#include "memb.hpp"
#include "diffboundary.hpp"

// STL headers
#include <vector>
#include <map>
#include <set>
////////////////////////////////////////////////////////////////////////////////

START_NAMESPACE(steps)
START_NAMESPACE(tetmesh)

////////////////////////////////////////////////////////////////////////////////

// Forward declarations
class TmPatch;
class TmComp;
class Memb;
class DiffBoundary;

enum ElementType {ELEM_VERTEX, ELEM_TRI, ELEM_TET, ELEM_UNDEFINED = 99};

struct ROISet {
    ROISet()
    {
        type = ELEM_UNDEFINED;
        indices = std::vector<uint> ();
    }

    ROISet(ElementType t, std::set<uint> const &i)
    {
        type = t;
        indices.assign(i.begin(), i.end());
    }
    
    ElementType                                         type;
    std::vector<uint>                                   indices;
};

////////////////////////////////////////////////////////////////////////////////

template <class T>
bool array_srt_cmp(T ar1[], T ar2[], uint ar_size);
bool bar_vec_contains(std::vector<uint> bars0, std::vector<uint> bars1);


/// Test whether id is a valid identifier for some named STEPS component.
/// It returns a boolean value.
///
/// A valid id must be at least 1 character long and must start with an
/// underscore or an alphabetical character (a to z, or A to Z). Following
/// characters can be any alphanumerical character or again underscores.
/// The id cannot contain spaces.
///
/// Examples of valid id's:
///     a, _a, _a_, a000, adasf0, FSDaa9
///
STEPS_EXTERN bool isValidID(std::string const & id);

/// Test whether id is a valid identifier for some named STEPS component.
///
/// This function calls steps::model::isValidID() for the test. But whereas
/// isValidID() returns true or false, checkID() raises a steps::ArgErr
/// exception if the id is not valid. This makes it useful for checking
/// input arguments.
///
STEPS_EXTERN void checkID(std::string const & id);

////////////////////////////////////////////////////////////////////////////////

/// The main container class for static tetrahedronl meshes.
/*!
This class stores the vertices points, tetrahedron and boundary triangles
that comprise the tetrahedronl mesh. In addition, it also precomputes
some auxiliary data for the mesh as a whole:

    - Rectangular, axis-aligned bounding box.
    - Overall volume

Auxiliary data is also stored for the tetrahedrons:

    - Volume of each tetrahedron.
    - For each tetrahedron, the indices of its 4 neighbouring tets.
      If there is no neighbour (i.e. if the tetrahedron lies on the
      border), this index will be -1. The sequence of neighbours is
      determined by the following common boundary triangles: (0,1,2);
      (0,1,3); (0,2,3); (1,2,3).
    - For each tetrahedron, the indices of its 4 neighbouring
      boundary triangles. The sequence of neighbours is also
      determined by (0,1,2); (0,1,3); (0,2,3); (1,2,3).
    - The compartment (Comp object) that a tetrahedron belongs to.
      Returns zero pointer if the tetrahedron has not been added to a comp
    - The total number of tetrahedron in the mesh
    - A method of finding which tetrahedron a point given in x,y,z
      coordinates belongs to

And for the triangles:

	- Area of each triangle.
    - Normal vector for each triangle, normalized to length 1.0.
    - For each triangle, the indices of its inside and outside
      neighbouring tetrahedron. If this tetrahedron does not exist
      (because the triangle lies on the outer boundary), this index
      will be -1.
    - The patch (Patch object) that a triangle belongs to. Returns
      zero pointer if triangle has not been added to a patch
    - The total number of triangles in the mesh

And, finally, for the vertices:
    - The total number of vertices in the mesh

NOTES:
    - Adding/deleting/moving vertices, triangles and tetrahedron after
      initiation is currently not implemented

    \warning Methods start with an underscore are not exposed to Python.
*/

class Tetmesh : public steps::wm::Geom
{

public:

	////////////////////////////////////////////////////////////////////////
	// OBJECT CONSTRUCTION & DESTRUCTION
	////////////////////////////////////////////////////////////////////////

	/* Disbaling this constructor because it has such a propensity for
	 * bugs and I son't want to maintain it any more
	 *
    /// Constructor
    ///
    /// \param nverts Number of vertices.
    /// \param ntets Number of tetrahedrons.
    /// \param ntris Number of triangles
    Tetmesh(uint nverts, uint ntets, uint ntris);
    */


    /// Constructor
    ///
    /// \param verts List of vertices.
    /// \param tets List of tetrahedrons.
    /// \param tris List of triangles.
    Tetmesh(std::vector<double> const & verts, std::vector<uint> const & tets,
    		std::vector<uint> const & tris = std::vector<uint>());

    /// Constructor
    ///
    /// \param verts
    /// TODO: finish this
    Tetmesh(std::vector<double> const & verts, std::vector<uint> const & tris,
    		std::vector<double> const & tri_areas,
    		std::vector<double> const & tri_norms,
    		std::vector<int> const & tri_tet_neighbs,
    		std::vector<uint> const & tets,
    		std::vector<double> const & tet_vols,
    		std::vector<double> const & tet_barycs,
    		std::vector<uint> const & tet_tri_neighbs,
    		std::vector<int> const & tet_tet_neighbs);

    /// Destructor
    virtual ~Tetmesh(void);

	////////////////////////////////////////////////////////////////////////
	// OPERATIONS (EXPOSED TO PYTHON): SETUP
	////////////////////////////////////////////////////////////////////////
    /// Setup a vertex.
    ///
    /// \param vidx Index of the vertex.
    /// \param x Coordinate x.
    /// \param y Coordinate y.
    /// \param z Coordinate z.
    void setVertex(uint vidx, double x, double y, double z);

    /// Setup a triangle.
    ///
    /// \param tidx Index of the triangle.
    /// \param vidx0 Index of vertex 0 that forms the triangle.
    /// \param vidx1 Index of vertex 1 that forms the triangle.
    /// \param vidx2 Index of vertex 2 that forms the triangle.
    void setTri(uint tidx, uint vidx0, uint vidx1, uint vidx2);

    /// Setup a tetrahedron.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \param vidx0 Index of vertex 0 that forms the tetrahedron.
    /// \param vidx1 Index of vertex 1 that forms the tetrahedron.
    /// \param vidx2 Index of vertex 2 that forms the tetrahedron.
    /// \param vidx3 Index of vertex 3 that forms the tetrahedron.
    void setTet(uint tidx, uint vidx0, uint vidx1, uint vidx2, uint vidx3);

    /// Setup the Temesh.
    void setup(void);

    /// Check if the Temesh is set up.
    ///
    /// \return True if the Temesh is set up;
    ///         False if else.
    bool isSetupDone(void) const
    { return pSetupDone; }
    
	
    ////////////////////////////////////////////////////////////////////////
	// DATA ACCESS (EXPOSED TO PYTHON): VERTICES
	////////////////////////////////////////////////////////////////////////

    /// Return the coordinates of a vertex with index vidx.
    ///
    /// \param vidx Index of the vertex.
    /// \return Coordinates of the vertex.
    std::vector<double> getVertex(uint vidx) const;

    /// Count the vertices in the Temesh.
    ///
    /// \return Number of the vertices.
    inline uint countVertices(void) const
    { return pVertsN; }

	////////////////////////////////////////////////////////////////////////
	// DATA ACCESS (EXPOSED TO PYTHON): BARS
	////////////////////////////////////////////////////////////////////////

    /// Return the bar with index bidx
    ///
    /// \param bidx Index of the bar.
    /// \return Indices of the two vertices that form the bar.
    std::vector<uint> getBar(uint bidx) const;

    /// Count the bars in the Tetmesh.
    ///
    /// \return Number of bars.
    inline uint countBars(void) const
    { return pBarsN; }

	////////////////////////////////////////////////////////////////////////
	// DATA ACCESS (EXPOSED TO PYTHON): TRIANGLES
	////////////////////////////////////////////////////////////////////////

    /// Return the triangle with index tidx
    ///
    /// \param tidx Index of the triangle.
    /// \return Indices of the vertices that form the triangle.
    std::vector<uint> getTri(uint tidx) const;

    /// Count the triangles in the Temesh.
    ///
    /// \return Number of the triangles.
    inline uint countTris(void) const
    { return pTrisN; }

    /// Return the area of a triangle with index tidx.
    ///
    /// \param tidx Index of the triangle.
    /// \return Area of the triangle.
    double getTriArea(uint tidx) const;

    /// Return the bars of a triangle
    ///
    /// \param tidx Index of the triangle
    /// \return Bars of the triangle
    std::vector<uint> getTriBars(uint tidx) const;

    /// Return the barycenter of triangle with index tidx
    ///
    /// \param tidx Index of the triangle.
    /// \return Barycenter of the triangle.
    std::vector<double> getTriBarycenter(uint tidx) const;

    /// Return the normalised triangle with index tidx
    ///
    /// \param tidx Index of the triangle.
    /// \return Coordinate of the normalised vertices form the triangle.
    std::vector<double> getTriNorm(uint tidx) const;

    //getTriBarycenter
    /// Return the patch which a triangle associated to.
    ///
    /// \param tidx Index of the triangle.
    /// \return Pointer to the patch.
    steps::tetmesh::TmPatch * getTriPatch(uint tidx) const;

    ///Set the patch which a triangle belongs to.
    ///
    /// \param tidx Index of the triangle.
    /// \param patch Pointer to the associated patch.
    void setTriPatch(uint tidx, steps::tetmesh::TmPatch * patch);

    ///Set the diffusion boundary which a triangle belongs to.
    ///
    /// \param tidx Index of the triangle.
    /// \param patch Pointer to the associated diffusion boundary.
    void setTriDiffBoundary(uint tidx, steps::tetmesh::DiffBoundary * diffb);

    /// Return the diffusion boundary which a triangle is associated to.
    ///
    /// \param tidx Index of the triangle.
    /// \return Pointer to the diffusion boundary.
    steps::tetmesh::DiffBoundary * getTriDiffBoundary(uint tidx) const;

    ///Return the tetrahedron neighbors of a triangle by its index.
    ///
    /// \param tidx Index of the triangle.
    /// \return Vector of the tetrahedron neighbors.
    ///
    std::vector<int> getTriTetNeighb(uint tidx) const;

    ///Return the 3 triangle neighbors within the same patch of a triangle by its index.
    ///
    /// \param tidx Index of the triangle.
    /// \param tmpatch Pointer to the patch
    /// \return Vector of the triangle neighbors.
    ///
    std::vector<int> getTriTriNeighb(uint tidx, TmPatch * tmpatch) const;

    ///Return all the triangle neighbors of a triangle by its index.
    ///
    /// \param tidx Index of the triangle.
    /// \return Set of the triangle neighbors.
    ///
    std::set<uint> getTriTriNeighbs(uint tidx) const;

    /// Flip the triangle's inner and outer tetrahedron.
    ///
    /// \param tidx Index of the triangle.
    void _flipTriTetNeighb(uint tidx);

    /// Flip the triangle's vertices and recalculate the normal.
    ///
    /// \param Index of the triangle.
    void _flipTriVerts(uint tidx);

	////////////////////////////////////////////////////////////////////////
	// DATA ACCESS (EXPOSED TO PYTHON): TETRAHEDRA
	////////////////////////////////////////////////////////////////////////
    /// Return a tetrahedron by its index.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return Vector of the indices of triangles which form the tetrahedron.
    std::vector<uint>  getTet(uint tidx) const;
    /// Count the number of tetrahedrons.
    ///
    /// \return Number of tetrahedrons.
    inline uint countTets(void) const
    { return pTetsN; }
    /// Return the volume of a tetrahedron by its index.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return Volume of the tetrahedron.

    double getTetVol(uint tidx) const;

    /// Computes the quality of the tetrahedron.
    ///
    /// This method uses the radius-edge ratio (RER) metric for tetrahedron
    /// quality, given by dividing the radius of the tetrahedron's
    /// circumsphere with the length of the shortest edge.
    ///
    /// The smaller this value, the more regular the tetrahedron. The
    /// lowest possible value of this metric is given by computing the
    /// RER for a fully regular tetrahedron:
    ///
    ///    Q = sqrt(6)/4 ~ 0.612
    ///
    /// This is a slightly weaker metric than getQualityAR, because
    /// certain slivers (degenerate tetrahedrons) can still have a fairly
    /// small value.
    ///
    /// \return Quality RER of the tetrahedron.
    double getTetQualityRER(uint tidx) const;

    /// Return the barycentre of the tetrahedron in x,y,z coordinates
    /// \param tidx Index of the tetrahedron
    /// \return Barycentre of the tetrahedron
	std::vector<double> getTetBarycenter(uint tidx) const;

    /// Return the compartment which a tetrahedron with index tidx belongs to.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return Pointer to the compartment object.

    steps::tetmesh::TmComp * getTetComp(uint tidx) const;
    ///Set the compartment which a tetrahedron with index tidx belongs to.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \param comp Pointer to the compartment object.

    void setTetComp(uint tidx, steps::tetmesh::TmComp * comp);
    ///Return the triangle neighbors of a tetrahedron with index tidx.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return Vector of the triangle neighbors.

    std::vector<uint> getTetTriNeighb(uint tidx) const;
    ///Return the tetrahedron neighbors of a tetrahedron with index tidx.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return Vector of the tetrahedron neighbors.

    std::vector<int> getTetTetNeighb(uint tidx) const;

    /// Find a tetrahedron which encompasses a given point.
    /// Return the index of the tetrahedron that encompasses point;
    ///  return -1 if point is outside mesh;
    /// if point is on boundary between two or more tetrahedron,
    /// returns first tetrahedron found.
    /// \param p A point given by its coordinates.
    /// \return ID of the found tetrahedron.

    int findTetByPoint(std::vector<double> p) const;
    

	////////////////////////////////////////////////////////////////////////
	// DATA ACCESS (EXPOSED TO PYTHON): MESH
	////////////////////////////////////////////////////////////////////////

    /// Return the minimal coordinate of the rectangular bounding box.
    ///
    /// \return Minimal coordinate of the rectangular bounding box.
    std::vector<double> getBoundMin(void) const;
    /// Return the maximal coordinate of the rectangular bounding box.
    ///
    /// \return Maximal coordinate of the rectangular bounding box.
    std::vector<double> getBoundMax(void) const;
    /// Return the total volume of the mesh.
    ///
    /// \return Volume of the mesh.
    double getMeshVolume(void) const;

    /// Return the triangles which form the surface boundary of the mesh.
    /// \return Vector of the triangle boundary.
    // Weiliang 2010.02.02
    std::vector<int> getSurfTris(void) const;

    ////////////////////////////////////////////////////////////////////////
	// Batch Data Access
	////////////////////////////////////////////////////////////////////////
    
    /// get barycentres of a list of tetrahedrons
    std::vector<double> getBatchTetBarycentres(std::vector<uint> const & tets) const;
    
    /// get barycentres of a list of tetrahedrons
    void getBatchTetBarycentresNP(unsigned int* indices, int input_size, double* centres, int output_size) const;
    
    /// get barycentres of a list of triangles
    std::vector<double> getBatchTriBarycentres(std::vector<uint> const & tris) const;
    
    /// get barycentres of a list of triangles
    void getBatchTriBarycentresNP(unsigned int* indices, int input_size, double* centres, int output_size) const;
    
    /// get coordinates of a list of vertices
    std::vector<double> getBatchVertices(std::vector<uint> const & verts) const;
    
    /// get coordinates of a list of vertices
    void getBatchVerticesNP(unsigned int* indices, int input_size, double* coordinates, int output_size) const;
    
    /// get vertex indices of a list of triangles
    std::vector<uint> getBatchTris(std::vector<uint> const & tris) const;
    
    /// get vertex indices of a list of triangles
    void getBatchTrisNP(unsigned int* t_indices, int input_size, unsigned int* v_indices, int output_size) const;
    
    /// get vertex indices of a list of tetrahedrons
    std::vector<uint> getBatchTets(std::vector<uint> const & tets) const;
    
    /// get vertex indices of a list of tetrahedrons
    void getBatchTetsNP(unsigned int* t_indices, int input_size, unsigned int* v_indices, int output_size) const;
    
    /// return the size of a set with unique vertex indices of a list of triangles
    /// preparation function for furture numpy data access
    uint getTriVerticesSetSizeNP(unsigned int* t_indices, int input_size) const;
    
    /// return the size of a set with unique vertex indices of a list of tetrahedrons
    /// preparation function for furture numpy data access
    uint getTetVerticesSetSizeNP(unsigned int* t_indices, int input_size) const;
    
    /// Get the set with unique vertex indices of a list of triangles, write into given 1D array
    void getTriVerticesMappingSetNP(unsigned int* t_indices, int input_size, unsigned int* t_vertices, int t_vertices_size, unsigned int* v_set, int v_set_size) const;
    
    /// Get the set with unique vertex indices of a list of tetrahedrons, write into given 1D array
    void getTetVerticesMappingSetNP(unsigned int* t_indices, int input_size, unsigned int* t_vertices, int t_vertices_size, unsigned int* v_set, int v_set_size) const;
    
    /// Generate npnts random points inside tetrahedron t_idx and write the coordinates to cords
    void genPointsInTet(unsigned tidx, unsigned npnts, double* cords, int cord_size) const;
    
    /// Generate npnts random points on triangle t_idx and write the coordinates to cords
    void genPointsInTri(unsigned tidx, unsigned npnts, double* cords, int cord_size) const;
    
    /// Generate the random points required in point_counts for tets in indices and store them in cords
    void genTetVisualPointsNP(unsigned int* indices, int index_size, unsigned int* point_counts, int count_size, double* cords, int cord_size) const;
    
    /// Generate the random points required in point_counts for tris in indices and store them in cords
    void genTriVisualPointsNP(unsigned int* indices, int index_size, unsigned int* point_counts, int count_size, double* cords, int cord_size) const;
    
    /// get the volumes of a list of tetrahedrons
    void getBatchTetVolsNP(unsigned int* indices, int index_size, double* volumes, int volume_size) const;
    
    /// get the areas of a list of triangles
    void getBatchTriAreasNP(unsigned int* indices, int index_size, double* areas, int area_size) const;
    
    /// reduce the number of points required to be generated in a list of tets based on maximum point density
    void reduceBatchTetPointCountsNP(unsigned int* indices, int index_size, unsigned int* point_counts, int count_size, double max_density);
    
    /// reduce the number of points required to be generated in a list of tris based on maximum point density
    void reduceBatchTriPointCountsNP(unsigned int* indices, int index_size, unsigned int* point_counts, int count_size, double max_density);
    
    /// Get tet neighbors for a list of tets, no duplication
    ///std::vector<int> getTetsTetNeighbSet(std::vector<uint> const & t_indices) const;
    
	////////////////////////////////////////////////////////////////////////
	// ROI (Region of Interest) Data
	////////////////////////////////////////////////////////////////////////
    
    /// Add a ROI data
    void addROI(std::string id, ElementType type, std::set<uint> const &indices);
    
    /// Remove a ROI data
    void removeROI(std::string id);
    
    /// Replace a ROI data with a new set with the same name
    void replaceROI(std::string id, ElementType type, std::set<uint> const &indices);
    
    /// Return the type of a ROI data
    ElementType getROIType(std::string id) const;
    
    /// Return the data of a ROI
    std::vector<uint> getROIData(std::string id) const;
    
    /// Return the data size of a ROI
    uint getROIDataSize(std::string id) const;
    
    /// get the total number of ROI recorded
    uint getNROIs(void);
    
    /// Return a ROI
    ROISet getROI(std::string id) const;
    
    /// get all ROI names
    std::vector<std::string> getAllROINames(void);
    
    /// return pointer of a ROI data
    uint* _getROIData(std::string id) const;
    
    /// check if a ROI enquire is valid
    bool checkROI(std::string id, ElementType type, uint count = 0, bool warning = true) const;
    
    ////////////////////////////////////////////////////////////////////////
	// ROI Data Access
	////////////////////////////////////////////////////////////////////////
    
    /// get barycentres of a list of tetrahedrons
    std::vector<double> getROITetBarycentres(std::string ROI_id) const;
    
    /// get barycentres of a list of tetrahedrons
    void getROITetBarycentresNP(std::string ROI_id, double* centres, int output_size) const;
    
    /// get barycentres of a list of triangles
    std::vector<double> getROITriBarycentres(std::string ROI_id) const;
    
    /// get barycentres of a list of triangles
    void getROITriBarycentresNP(std::string ROI_id, double* centres, int output_size) const;
    
    /// get coordinates of a list of vertices
    std::vector<double> getROIVertices(std::string ROI_id) const;
    
    /// get coordinates of a list of vertices
    void getROIVerticesNP(std::string ROI_id, double* coordinates, int output_size) const;
    
    /// get vertex indices of a list of triangles
    std::vector<uint> getROITris(std::string ROI_id) const;
    
    /// get vertex indices of a list of triangles
    void getROITrisNP(std::string ROI_id, unsigned int* v_indices, int output_size) const;
    
    /// get vertex indices of a list of tetrahedrons
    std::vector<uint> getROITets(std::string ROI_id) const;
    
    /// get vertex indices of a list of tetrahedrons
    void getROITetsNP(std::string ROI_id, unsigned int* v_indices, int output_size) const;
    
    /// return the size of a set with unique vertex indices of a list of triangles
    /// preparation function for furture numpy data access
    uint getROITriVerticesSetSizeNP(std::string ROI_id) const;
    
    /// return the size of a set with unique vertex indices of a list of tetrahedrons
    /// preparation function for furture numpy data access
    uint getROITetVerticesSetSizeNP(std::string ROI_id) const;
    
    /// Get the set with unique vertex indices of a list of triangles, write into given 1D array
    void getROITriVerticesMappingSetNP(std::string ROI_id, unsigned int* t_vertices, int t_vertices_size, unsigned int* v_set, int v_set_size) const;
    
    /// Get the set with unique vertex indices of a list of tetrahedrons, write into given 1D array
    void getROITetVerticesMappingSetNP(std::string ROI_id, unsigned int* t_vertices, int t_vertices_size, unsigned int* v_set, int v_set_size) const;
    
    /// Generate the random points required in point_counts for tets in indices and store them in cords
    void genROITetVisualPointsNP(std::string ROI_id, unsigned int* point_counts, int count_size, double* cords, int cord_size) const;
    
    /// Generate the random points required in point_counts for tris in indices and store them in cords
    void genROITriVisualPointsNP(std::string ROI_id, unsigned int* point_counts, int count_size, double* cords, int cord_size) const;
    
    /// get the volumes of a list of tetrahedrons
    void getROITetVolsNP(std::string ROI_id, double* volumes, int volume_size) const;
    
    /// get the areas of a list of triangles
    void getROITriAreasNP(std::string ROI_id, double* areas, int area_size) const;
    
    /// reduce the number of points required to be generated in a list of tets based on maximum point density
    void reduceROITetPointCountsNP(std::string ROI_id, unsigned int* point_counts, int count_size, double max_density);
    
    /// reduce the number of points required to be generated in a list of tris based on maximum point density
    void reduceROITriPointCountsNP(std::string ROI_id, unsigned int* point_counts, int count_size, double max_density);
    
    ////////////////////////////////////////////////////////////////////////
    // DATA ACCESS (C++ INTERNAL)
    ////////////////////////////////////////////////////////////////////////

    /// Return a vertex with index vidx.
    ///
    /// \param vidx Index of the vertex.
    /// \return Coordinates of the vertex.
    double * _getVertex(uint vidx) const;

    /// Return a triangle with index tidx.
    ///
    /// \param tidx Index of the triangle.
    /// \return List of the vertices form the triangle.
    uint * _getTri(uint tidx) const;

    /// Return a tetrahedron with index tidx.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return List of the vertices form the tetrahedron.
    uint * _getTet(uint tidx) const;

    ///Return the tetrahedron neighbors of a triangle with index tidx.
    ///
    /// \param tidx Index of the triangle.
    /// \return Array of the tetrahedron neighbors.
    int * _getTriTetNeighb(uint tidx) const;

    ///Return the triangle neighbors of a tetrahedron with index tidx.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return Array of the triangle neighbors.
    uint * _getTetTriNeighb(uint tidx) const;

    ///Return the tetrahedron neighbors of a tetrahedron with index tidx.
    ///
    /// \param tidx Index of the tetrahedron.
    /// \return Array of the tetrahedron neighbors.
    int * _getTetTetNeighb(uint tidx) const;

    /// Return the normalised triangle with index tidx
    ///
    /// \param tidx Index of the triangle.
    /// \return Array of Coordinate of the normalised vertices form the triangle.
    double * _getTriNorm(uint tidx) const;

    ////////////////////////////////////////////////////////////////////////

    /// Check if a membrane id is occupied.
    ///
    /// \param id ID of the membrane.
    void _checkMembID(std::string const & id) const;

    /// Change the id of a membrane.
    ///
    /// \param o Old id of the membrane.
    /// \param n New id of the membrane.
    void _handleMembIDChange(std::string const & o, std::string const & n);

    /// Add a membrane.
    ///
    /// \param memb Pointer to the membrane.
    void _handleMembAdd(steps::tetmesh::Memb * memb);

    /// Delete a membrane.
    ///
    /// \param patch Pointer to the membrane.
    void _handleMembDel(steps::tetmesh::Memb * memb);

	////////////////////////////////////////////////////////////////////////
	// INTERNAL (NON-EXPOSED): SOLVER HELPER METHODS
	////////////////////////////////////////////////////////////////////////

    /// Count the membranes in the tetmesh container.
    ///
    /// \return Number of membranes.
	inline uint _countMembs(void) const
	{ return pMembs.size(); }

    /// Return a membrane with index gidx.
    ///
    /// \param gidx Index of the membrane.
    /// \return Pointer to the membrane.
	steps::tetmesh::Memb * _getMemb(uint gidx) const;

    ////////////////////////////////////////////////////////////////////////

    /// Check if a diffusion boundary id is occupied.
    ///
    /// \param id ID of the diffusion boundary.
    void _checkDiffBoundaryID(std::string const & id) const;

    /// Change the id of a diffusion boundary.
    ///
    /// \param o Old id of the diffusion boundary.
    /// \param n New id of the diffusion boundary.
    void _handleDiffBoundaryIDChange(std::string const & o, std::string const & n);

    /// Add a diffusion boundary.
    ///
    /// \param patch Pointer to the diffusion boundary.
    void _handleDiffBoundaryAdd(steps::tetmesh::DiffBoundary * diffb);

    /// Delete a diffusion boundary.
    ///
    /// \param patch Pointer to the diffusion boundary.
    void _handleDiffBoundaryDel(steps::tetmesh::DiffBoundary * diffb);

    /// Count the diffusion boundaries in the tetmesh container.
    ///
    /// \return Number of diffusion boundaries.
	inline uint _countDiffBoundaries(void) const
	{ return pDiffBoundaries.size(); }

    /// Return a diffusion boundary with index gidx.
    ///
    /// \param gidx Index of the diffusion boundary.
    /// \return Pointer to the diffusion boundary.
	steps::tetmesh::DiffBoundary * _getDiffBoundary(uint gidx) const;


private:

    ////////////////////////////////////////////////////////////////////////

    bool                                pSetupDone;

    ///////////////////////// DATA: VERTICES ///////////////////////////////
    ///
    /// The total number of vertices in the mesh
    uint                                pVertsN;
    /// The vertices by x,y,z coordinates
    double                            * pVerts;

    /////////////////////////// DATA: BARS /////////////////////////////////
    ///
    /// The total number of 1D 'bars' in the mesh
    uint 								pBarsN;
    /// The bars by the two vertices index
    uint 							  * pBars;

    ///////////////////////// DATA: TRIANGLES //////////////////////////////
    ///
    /// The total number of triangles in the mesh
    uint                                pTrisN;
    /// The triangles by vertices index
    uint                              * pTris;
    /// Array available for user-supplied triangle data for 2nd constructor
    uint                              * pTris_user;
    // The bars of the triangle
    uint 							  * pTri_bars;
    /// The areas of the triangles
    double                            * pTri_areas;
    /// The triangle barycenters
    double                            * pTri_barycs;
    /// The triangle normals
    double                            * pTri_norms;
    /// The patch a triangle belongs to
    steps::tetmesh::TmPatch          ** pTri_patches;

    /// The diffusion boundary a triangle belongs to
    steps::tetmesh::DiffBoundary 	 ** pTri_diffboundaries;

    /// The tetrahedron neighbours of each triangle (by index)
    int                               * pTri_tet_neighbours;

    ///////////////////////// DATA: TETRAHEDRA /////////////////////////////
    ///
    /// The total number of tetrahedron in the mesh
    uint                                pTetsN;
    /// The tetrahedron by vertices index
    uint                              * pTets;
    /// The volume of the tetrahedron
    double                            * pTet_vols;
	/// The barycentres of the tetrahedra
	double                            * pTet_barycentres;
    /// The compartment a tetrahedron belongs to
    steps::tetmesh::TmComp           ** pTet_comps;
    /// The triangle neighbours of each tetrahedron (by index)
    uint                              * pTet_tri_neighbours;
    /// The tetrahedron neighbours of each tetrahedron (by index)
    int                               * pTet_tet_neighbours;

    ////////////////////////////////////////////////////////////////////////

    /// Information about the minimal and maximal boundary values
    ///
    double                      pXmin;
    double                      pXmax;
    double                      pYmin;
    double                      pYmax;
    double                      pZmin;
    double                      pZmax;

    ////////////////////////////////////////////////////////////////////////

    // List of contained membranes. Members of this class because they
    // do not belong in a well-mixed geometry description
    std::map<std::string, steps::tetmesh::Memb *>       pMembs;


	std::map<std::string, steps::tetmesh::DiffBoundary *> pDiffBoundaries;


    ////////////////////////////////////////////////////////////////////////
    
    ////////////////////////// ROI Dataset /////////////////////////////////
    std::map<std::string, ROISet>                       mROI;

};

////////////////////////////////////////////////////////////////////////////////

END_NAMESPACE(tetmesh)
END_NAMESPACE(steps)

#endif

// STEPS_TETMESH_TETMESH_HPP
// END
