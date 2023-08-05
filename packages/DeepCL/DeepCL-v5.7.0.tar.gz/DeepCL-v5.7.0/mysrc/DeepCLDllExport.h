#pragma once

#if defined(_WIN32) 
# if defined(DeepCL_EXPORTS)
#  define DeepCL_EXPORT __declspec(dllexport)
# else
#  define DeepCL_EXPORT __declspec(dllimport)
# endif // DeepCL_EXPORTS
#else // _WIN32
# define DeepCL_EXPORT
#endif

// does nothing, just a marker, means it is part of
// our semantic versioning 'stable' api
#define PUBLICAPI

typedef unsigned char uchar;

