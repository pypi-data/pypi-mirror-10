
#include <stdio.h>
#include <stddef.h>
#include <stdarg.h>
#include <errno.h>
#include <sys/types.h>   /* XXX for ssize_t on some platforms */

/* this block of #ifs should be kept exactly identical between
   c/_cffi_backend.c, cffi/vengine_cpy.py, cffi/vengine_gen.py */
#if defined(_MSC_VER)
# include <malloc.h>   /* for alloca() */
# if _MSC_VER < 1600   /* MSVC < 2010 */
   typedef __int8 int8_t;
   typedef __int16 int16_t;
   typedef __int32 int32_t;
   typedef __int64 int64_t;
   typedef unsigned __int8 uint8_t;
   typedef unsigned __int16 uint16_t;
   typedef unsigned __int32 uint32_t;
   typedef unsigned __int64 uint64_t;
# else
#  include <stdint.h>
# endif
# if _MSC_VER < 1800   /* MSVC < 2013 */
   typedef unsigned char _Bool;
# endif
#else
# include <stdint.h>
# if (defined (__SVR4) && defined (__sun)) || defined(_AIX)
#  include <alloca.h>
# endif
#endif


    #include "ring.c"
    
void _cffi_f_ring_add(CPersistentRing * x0, CPersistentRing * x1)
{
  ring_add(x0, x1);
}

void _cffi_f_ring_del(CPersistentRing * x0)
{
  ring_del(x0);
}

void _cffi_f_ring_move_to_head(CPersistentRing * x0, CPersistentRing * x1)
{
  ring_move_to_head(x0, x1);
}

static void _cffi_check_struct_CPersistentRing_struct(struct CPersistentRing_struct *p)
{
  /* only to generate compile-time warnings or errors */
  { CPersistentRing * *tmp = &p->r_prev; (void)tmp; }
  { CPersistentRing * *tmp = &p->r_next; (void)tmp; }
}
intptr_t _cffi_layout_struct_CPersistentRing_struct(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct CPersistentRing_struct y; };
  static intptr_t nums[] = {
    sizeof(struct CPersistentRing_struct),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct CPersistentRing_struct, r_prev),
    sizeof(((struct CPersistentRing_struct *)0)->r_prev),
    offsetof(struct CPersistentRing_struct, r_next),
    sizeof(((struct CPersistentRing_struct *)0)->r_next),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_CPersistentRing_struct(0);
}

