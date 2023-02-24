# Autogenerated file, do not edit, this file provides stubs for builtins autocomplete in VSCode, PyCharm, etc

from typing import Any
from typing import Tuple
from typing import Callable
from typing import overload


from warp.types import array, array2d, array3d, array4d, constant
from warp.types import int8, uint8, int16, uint16, int32, uint32, int64, uint64, float16, float32, float64
from warp.types import vec, mat, quaternion
from warp.types import vec2, vec2ub, vec2h, vec2f, vec2d
from warp.types import vec3, vec3ub, vec3h, vec3f, vec3d
from warp.types import vec4, vec4ub, vec4h, vec4f, vec4d
from warp.types import mat22, mat22h, mat22f, mat22d
from warp.types import mat33, mat33h, mat33f, mat33d
from warp.types import mat44, mat44h, mat44f, mat44d
from warp.types import quat, quath, quatf, quatd
from warp.types import transform, transformh, transformf, transformd
from warp.types import spatial_vector, spatial_vectorh, spatial_vectorf, spatial_vectord
from warp.types import spatial_matrix, spatial_matrixh, spatial_matrixf, spatial_matrixd
from warp.types import Bvh, Mesh, HashGrid, Volume, MarchingCubes
from warp.types import bvh_query_t, mesh_query_aabb_t, hash_grid_query_t
from warp.types import matmul, adj_matmul, batched_matmul, adj_batched_matmul, from_ptr

from warp.context import init, func, kernel, struct
from warp.context import is_cpu_available, is_cuda_available, is_device_available
from warp.context import get_devices, get_preferred_device
from warp.context import get_cuda_devices, get_cuda_device_count, get_cuda_device, map_cuda_device, unmap_cuda_device
from warp.context import get_device, set_device, synchronize_device
from warp.context import zeros, zeros_like, clone, empty, empty_like, copy, from_numpy, launch, synchronize, force_load
from warp.context import set_module_options, get_module_options, get_module
from warp.context import capture_begin, capture_end, capture_launch
from warp.context import print_builtins, export_builtins, export_stubs
from warp.context import Kernel, Function
from warp.context import Stream, get_stream, set_stream, synchronize_stream
from warp.context import Event, record_event, wait_event, wait_stream

from warp.tape import Tape
from warp.utils import ScopedTimer, ScopedCudaGuard, ScopedDevice, ScopedStream
from warp.utils import transform_expand

from warp.torch import from_torch, to_torch
from warp.torch import device_from_torch, device_to_torch
from warp.torch import stream_from_torch, stream_to_torch

from warp.jax import from_jax, to_jax
from warp.jax import device_from_jax, device_to_jax

from warp.dlpack import from_dlpack, to_dlpack

from warp.constants import *

from . import builtins, render



@overload
def spatial_jacobian(S: array[vector_t], joint_parents: array[int32], joint_qd_start: array[int32], joint_start: int32, joint_count: int32, J_start: int32, J_out: array[Float]):
   """

   """
   ...

@overload
def spatial_mass(I_s: array[matrix_t], joint_start: int32, joint_count: int32, M_start: int32, M: array[Float]):
   """

   """
   ...

@overload
def mlp(weights: array[float32], bias: array[float32], activation: Callable, index: int32, x: array[float32], out: array[float32]):
   """
   Evaluate a multi-layer perceptron (MLP) layer in the form: ``out = act(weights*x + bias)``. 

      :param weights: A layer's network weights with dimensions ``(m, n)``.
      :param bias: An array with dimensions ``(n)``.
      :param activation: A ``wp.func`` function that takes a single scalar float as input and returns a scalar float as output
      :param index: The batch item to process, typically each thread will process 1 item in the batch, in this case index should be ``wp.tid()``
      :param x: The feature matrix with dimensions ``(n, b)``
      :param out: The network output with dimensions ``(m, b)``

      :note: Feature and output matrices are transposed compared to some other frameworks such as PyTorch. All matrices are assumed to be stored in flattened row-major memory layout (NumPy default).
   """
   ...

@overload
def bvh_query_aabb(id: uint64, lower: vec3, upper: vec3) -> bvh_query_t:
   """
   Construct an axis-aligned bounding box query against a bvh object. This query can be used to iterate over all bounds
      inside a bvh. Returns an object that is used to track state during bvh traversal.
    
      :param id: The bvh identifier
      :param lower: The lower bound of the bounding box in bvh space
      :param upper: The upper bound of the bounding box in bvh space
   """
   ...

@overload
def bvh_query_ray(id: uint64, start: vec3, dir: vec3) -> bvh_query_t:
   """
   Construct a ray query against a bvh object. This query can be used to iterate over all bounds
      that intersect the ray. Returns an object that is used to track state during bvh traversal.
    
      :param id: The bvh identifier
      :param start: The start of the ray in bvh space
      :param dir: The direction of the ray in bvh space
   """
   ...

@overload
def bvh_query_next(query: bvh_query_t, index: int32) -> bool:
   """
   Move to the next bound returned by the query. The index of the current bound is stored in ``index``, returns ``False``
      if there are no more overlapping bound.
   """
   ...

@overload
def mesh_query_point(id: uint64, point: vec3, max_dist: float32, inside: float32, face: int32, bary_u: float32, bary_v: float32) -> bool:
   """
   Computes the closest point on the mesh with identifier `id` to the given point in space. Returns ``True`` if a point < ``max_dist`` is found.

      :param id: The mesh identifier
      :param point: The point in space to query
      :param max_dist: Mesh faces above this distance will not be considered by the query
      :param inside: Returns a value < 0 if query point is inside the mesh, >=0 otherwise. Note that mesh must be watertight for this to be robust
      :param face: Returns the index of the closest face
      :param bary_u: Returns the barycentric u coordinate of the closest point
      :param bary_v: Retruns the barycentric v coordinate of the closest point
   """
   ...

@overload
def mesh_query_ray(id: uint64, start: vec3, dir: vec3, max_t: float32, t: float32, bary_u: float32, bary_v: float32, sign: float32, normal: vec3, face: int32) -> bool:
   """
   Computes the closest ray hit on the mesh with identifier `id`, returns ``True`` if a point < ``max_t`` is found.

      :param id: The mesh identifier
      :param start: The start point of the ray
      :param dir: The ray direction (should be normalized)
      :param max_t: The maximum distance along the ray to check for intersections
      :param t: Returns the distance of the closest hit along the ray
      :param bary_u: Returns the barycentric u coordinate of the closest hit
      :param bary_v: Returns the barycentric v coordinate of the closest hit
      :param sign: Returns a value > 0 if the hit ray hit front of the face, returns < 0 otherwise
      :param normal: Returns the face normal
      :param face: Returns the index of the hit face
   """
   ...

@overload
def mesh_query_aabb(id: uint64, lower: vec3, upper: vec3) -> mesh_query_aabb_t:
   """
   Construct an axis-aligned bounding box query against a mesh object. This query can be used to iterate over all triangles
      inside a volume. Returns an object that is used to track state during mesh traversal.
    
      :param id: The mesh identifier
      :param lower: The lower bound of the bounding box in mesh space
      :param upper: The upper bound of the bounding box in mesh space
   """
   ...

@overload
def mesh_query_aabb_next(query: mesh_query_aabb_t, index: int32) -> bool:
   """
   Move to the next triangle overlapping the query bounding box. The index of the current face is stored in ``index``, returns ``False``
      if there are no more overlapping triangles.
   """
   ...

@overload
def mesh_eval_position(id: uint64, face: int32, bary_u: float32, bary_v: float32) -> vec3:
   """
   Evaluates the position on the mesh given a face index, and barycentric coordinates.
   """
   ...

@overload
def mesh_eval_velocity(id: uint64, face: int32, bary_u: float32, bary_v: float32) -> vec3:
   """
   Evaluates the velocity on the mesh given a face index, and barycentric coordinates.
   """
   ...

@overload
def hash_grid_query(id: uint64, point: vec3, max_dist: float32) -> hash_grid_query_t:
   """
   Construct a point query against a hash grid. This query can be used to iterate over all neighboring points withing a 
      fixed radius from the query point. Returns an object that is used to track state during neighbor traversal.
   """
   ...

@overload
def hash_grid_query_next(query: hash_grid_query_t, index: int32) -> bool:
   """
   Move to the next point in the hash grid query. The index of the current neighbor is stored in ``index``, returns ``False``
      if there are no more neighbors.
   """
   ...

@overload
def hash_grid_point_id(id: uint64, index: int32) -> int:
   """
   Return the index of a point in the grid, this can be used to re-order threads such that grid 
      traversal occurs in a spatially coherent order.
   """
   ...

@overload
def intersect_tri_tri(v0: vec3, v1: vec3, v2: vec3, u0: vec3, u1: vec3, u2: vec3) -> int:
   """
   Tests for intersection between two triangles (v0, v1, v2) and (u0, u1, u2) using Moller's method. Returns > 0 if triangles intersect.
   """
   ...

@overload
def mesh_get(id: uint64) -> Mesh:
   """
   Retrieves the mesh given its index.
   """
   ...

@overload
def mesh_eval_face_normal(id: uint64, face: int32) -> vec3:
   """
   Evaluates the face normal the mesh given a face index.
   """
   ...

@overload
def mesh_get_point(id: uint64, index: int32) -> vec3:
   """
   Returns the point of the mesh given a index.
   """
   ...

@overload
def mesh_get_velocity(id: uint64, index: int32) -> vec3:
   """
   Returns the velocity of the mesh given a index.
   """
   ...

@overload
def mesh_get_index(id: uint64, index: int32) -> int:
   """
   Returns the point-index of the mesh given a face-vertex index.
   """
   ...

@overload
def closest_point_edge_edge(p1: vec3, q1: vec3, p2: vec3, q2: vec3, epsilon: float32) -> vec3:
   """
   Finds the closest points between two edges. Returns barycentric weights to the points on each edge, as well as the closest distance between the edges.

      :param p1: First point of first edge
      :param q1: Second point of first edge
      :param p2: First point of second edge
      :param q2: Second point of second edge
      :param epsilon: Zero tolerance for determining if points in an edge are degenerate.
      :param out: vec3 output containing (s,t,d), where `s` in [0,1] is the barycentric weight for the first edge, `t` is the barycentric weight for the second edge, and `d` is the distance between the two edges at these two closest points.
   """
   ...

@overload
def volume_sample_f(id: uint64, uvw: vec3, sampling_mode: int32) -> float:
   """
   Sample the volume given by ``id`` at the volume local-space point ``uvw``. Interpolation should be ``wp.Volume.CLOSEST``, or ``wp.Volume.LINEAR.``
   """
   ...

@overload
def volume_lookup_f(id: uint64, i: int32, j: int32, k: int32) -> float:
   """
   Returns the value of voxel with coordinates ``i``, ``j``, ``k``, if the voxel at this index does not exist this function returns the background value
   """
   ...

@overload
def volume_store_f(id: uint64, i: int32, j: int32, k: int32, value: float32):
   """
   Store the value at voxel with coordinates ``i``, ``j``, ``k``.
   """
   ...

@overload
def volume_sample_v(id: uint64, uvw: vec3, sampling_mode: int32) -> vec3:
   """
   Sample the vector volume given by ``id`` at the volume local-space point ``uvw``. Interpolation should be ``wp.Volume.CLOSEST``, or ``wp.Volume.LINEAR.``
   """
   ...

@overload
def volume_lookup_v(id: uint64, i: int32, j: int32, k: int32) -> vec3:
   """
   Returns the vector value of voxel with coordinates ``i``, ``j``, ``k``, if the voxel at this index does not exist this function returns the background value
   """
   ...

@overload
def volume_store_v(id: uint64, i: int32, j: int32, k: int32, value: vec3):
   """
   Store the value at voxel with coordinates ``i``, ``j``, ``k``.
   """
   ...

@overload
def volume_sample_i(id: uint64, uvw: vec3) -> int:
   """
   Sample the int32 volume given by ``id`` at the volume local-space point ``uvw``. 
   """
   ...

@overload
def volume_lookup_i(id: uint64, i: int32, j: int32, k: int32) -> int:
   """
   Returns the int32 value of voxel with coordinates ``i``, ``j``, ``k``, if the voxel at this index does not exist this function returns the background value
   """
   ...

@overload
def volume_store_i(id: uint64, i: int32, j: int32, k: int32, value: int32):
   """
   Store the value at voxel with coordinates ``i``, ``j``, ``k``.
   """
   ...

@overload
def volume_index_to_world(id: uint64, uvw: vec3) -> vec3:
   """
   Transform a point defined in volume index space to world space given the volume's intrinsic affine transformation.
   """
   ...

@overload
def volume_world_to_index(id: uint64, xyz: vec3) -> vec3:
   """
   Transform a point defined in volume world space to the volume's index space, given the volume's intrinsic affine transformation.
   """
   ...

@overload
def volume_index_to_world_dir(id: uint64, uvw: vec3) -> vec3:
   """
   Transform a direction defined in volume index space to world space given the volume's intrinsic affine transformation.
   """
   ...

@overload
def volume_world_to_index_dir(id: uint64, xyz: vec3) -> vec3:
   """
   Transform a direction defined in volume world space to the volume's index space, given the volume's intrinsic affine transformation.
   """
   ...

@overload
def rand_init(seed: int32) -> uint32:
   """
   Initialize a new random number generator given a user-defined seed. Returns a 32-bit integer representing the RNG state.
   """
   ...

@overload
def rand_init(seed: int32, offset: int32) -> uint32:
   """
   Initialize a new random number generator given a user-defined seed and an offset. 
      This alternative constructor can be useful in parallel programs, where a kernel as a whole should share a seed,
      but each thread should generate uncorrelated values. In this case usage should be ``r = rand_init(seed, tid)``
   """
   ...

@overload
def randi(state: uint32) -> int:
   """
   Return a random integer between [0, 2^32)
   """
   ...

@overload
def randi(state: uint32, min: int32, max: int32) -> int:
   """
   Return a random integer between [min, max)
   """
   ...

@overload
def randf(state: uint32) -> float:
   """
   Return a random float between [0.0, 1.0)
   """
   ...

@overload
def randf(state: uint32, min: float32, max: float32) -> float:
   """
   Return a random float between [min, max)
   """
   ...

@overload
def randn(state: uint32) -> float:
   """
   Sample a normal distribution
   """
   ...

@overload
def sample_cdf(state: uint32, cdf: array[float32]) -> int:
   """
   Inverse transform sample a cumulative distribution function
   """
   ...

@overload
def sample_triangle(state: uint32) -> vec2:
   """
   Uniformly sample a triangle. Returns sample barycentric coordinates
   """
   ...

@overload
def sample_unit_ring(state: uint32) -> vec2:
   """
   Uniformly sample a ring in the xy plane
   """
   ...

@overload
def sample_unit_disk(state: uint32) -> vec2:
   """
   Uniformly sample a disk in the xy plane
   """
   ...

@overload
def sample_unit_sphere_surface(state: uint32) -> vec3:
   """
   Uniformly sample a unit sphere surface
   """
   ...

@overload
def sample_unit_sphere(state: uint32) -> vec3:
   """
   Uniformly sample a unit sphere
   """
   ...

@overload
def sample_unit_hemisphere_surface(state: uint32) -> vec3:
   """
   Uniformly sample a unit hemisphere surface
   """
   ...

@overload
def sample_unit_hemisphere(state: uint32) -> vec3:
   """
   Uniformly sample a unit hemisphere
   """
   ...

@overload
def sample_unit_square(state: uint32) -> vec2:
   """
   Uniformly sample a unit square
   """
   ...

@overload
def sample_unit_cube(state: uint32) -> vec3:
   """
   Uniformly sample a unit cube
   """
   ...

@overload
def noise(state: uint32, x: float32) -> float:
   """
   Non-periodic Perlin-style noise in 1d.
   """
   ...

@overload
def noise(state: uint32, xy: vec2) -> float:
   """
   Non-periodic Perlin-style noise in 2d.
   """
   ...

@overload
def noise(state: uint32, xyz: vec3) -> float:
   """
   Non-periodic Perlin-style noise in 3d.
   """
   ...

@overload
def noise(state: uint32, xyzt: vec4) -> float:
   """
   Non-periodic Perlin-style noise in 4d.
   """
   ...

@overload
def pnoise(state: uint32, x: float32, px: int32) -> float:
   """
   Periodic Perlin-style noise in 1d.
   """
   ...

@overload
def pnoise(state: uint32, xy: vec2, px: int32, py: int32) -> float:
   """
   Periodic Perlin-style noise in 2d.
   """
   ...

@overload
def pnoise(state: uint32, xyz: vec3, px: int32, py: int32, pz: int32) -> float:
   """
   Periodic Perlin-style noise in 3d.
   """
   ...

@overload
def pnoise(state: uint32, xyzt: vec4, px: int32, py: int32, pz: int32, pt: int32) -> float:
   """
   Periodic Perlin-style noise in 4d.
   """
   ...

@overload
def curlnoise(state: uint32, xy: vec2) -> vec2:
   """
   Divergence-free vector field based on the gradient of a Perlin noise function.
   """
   ...

@overload
def curlnoise(state: uint32, xyz: vec3) -> vec3:
   """
   Divergence-free vector field based on the curl of three Perlin noise functions.
   """
   ...

@overload
def curlnoise(state: uint32, xyzt: vec4) -> vec3:
   """
   Divergence-free vector field based on the curl of three Perlin noise functions.
   """
   ...

@overload
def printf():
   """
   Allows printing formatted strings, using C-style format specifiers.
   """
   ...

@overload
def tid() -> int:
   """
   Return the current thread index. Note that this is the *global* index of the thread in the range [0, dim) 
      where dim is the parameter passed to kernel launch.
   """
   ...

@overload
def tid() -> Tuple[int, int]:
   """
   Return the current thread indices for a 2d kernel launch. Use ``i,j = wp.tid()`` syntax to retrieve the coordinates inside the kernel thread grid.
   """
   ...

@overload
def tid() -> Tuple[int, int, int]:
   """
   Return the current thread indices for a 3d kernel launch. Use ``i,j,k = wp.tid()`` syntax to retrieve the coordinates inside the kernel thread grid.
   """
   ...

@overload
def tid() -> Tuple[int, int, int, int]:
   """
   Return the current thread indices for a 4d kernel launch. Use ``i,j,k,l = wp.tid()`` syntax to retrieve the coordinates inside the kernel thread grid.
   """
   ...

@overload
def select(cond: bool, arg1: Any, arg2: Any):
   """
   Select between two arguments, if cond is false then return ``arg1``, otherwise return ``arg2``
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by index.
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, j: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, j: int32, k: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_add(a: array[Any], i: int32, j: int32, k: int32, l: int32, value: Any):
   """
   Atomically add ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by index.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, j: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, j: int32, k: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_sub(a: array[Any], i: int32, j: int32, k: int32, l: int32, value: Any):
   """
   Atomically subtract ``value`` onto the array at location given by indices.
   """
   ...

@overload
def atomic_min(a: array[Any], i: int32, value: Any):
   """
   Compute the minimum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def atomic_min(a: array[Any], i: int32, j: int32, value: Any):
   """
   Compute the minimum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def atomic_min(a: array[Any], i: int32, j: int32, k: int32, value: Any):
   """
   Compute the minimum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def atomic_min(a: array[Any], i: int32, j: int32, k: int32, l: int32, value: Any):
   """
   Compute the minimum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def atomic_max(a: array[Any], i: int32, value: Any):
   """
   Compute the maximum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def atomic_max(a: array[Any], i: int32, j: int32, value: Any):
   """
   Compute the maximum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def atomic_max(a: array[Any], i: int32, j: int32, k: int32, value: Any):
   """
   Compute the maximum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def atomic_max(a: array[Any], i: int32, j: int32, k: int32, l: int32, value: Any):
   """
   Compute the maximum of ``value`` and ``array[index]`` and atomically update the array. Note that for vectors and matrices the operation is only atomic on a per-component basis.
   """
   ...

@overload
def expect_eq(arg1: int8, arg2: int8):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint8, arg2: uint8):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: int16, arg2: int16):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint16, arg2: uint16):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: int32, arg2: int32):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint32, arg2: uint32):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: int64, arg2: int64):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: uint64, arg2: uint64):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: float16, arg2: float16):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: float32, arg2: float32):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: float64, arg2: float64):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: quath, arg2: quath):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: quatf, arg2: quatf):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: quatd, arg2: quatd):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: quat, arg2: quat):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: transformh, arg2: transformh):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: transformf, arg2: transformf):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: transformd, arg2: transformd):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_eq(arg1: transform, arg2: transform):
   """
   Prints an error to stdout if arg1 and arg2 are not equal
   """
   ...

@overload
def expect_near(arg1: vec3, arg2: vec3, tolerance: float32):
   """
   Prints an error to stdout if any element of arg1 and arg2 are not closer than tolerance in magnitude
   """
   ...

@overload
def unot(b: bool) -> bool:
   """

   """
   ...

