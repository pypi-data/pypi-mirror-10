
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
   typedef __int8 int_least8_t;
   typedef __int16 int_least16_t;
   typedef __int32 int_least32_t;
   typedef __int64 int_least64_t;
   typedef unsigned __int8 uint_least8_t;
   typedef unsigned __int16 uint_least16_t;
   typedef unsigned __int32 uint_least32_t;
   typedef unsigned __int64 uint_least64_t;
   typedef __int8 int_fast8_t;
   typedef __int16 int_fast16_t;
   typedef __int32 int_fast32_t;
   typedef __int64 int_fast64_t;
   typedef unsigned __int8 uint_fast8_t;
   typedef unsigned __int16 uint_fast16_t;
   typedef unsigned __int32 uint_fast32_t;
   typedef unsigned __int64 uint_fast64_t;
   typedef __int64 intmax_t;
   typedef unsigned __int64 uintmax_t;
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

   // passed to the real C compiler
#define LIBEV_EMBED 1
#include "libev.h"

static void
_gevent_noop(struct ev_loop *_loop, struct ev_timer *w, int revents) { }

void (*gevent_noop)(struct ev_loop *, struct ev_timer *, int) = &_gevent_noop;

static int (*python_callback)(void* handle, int revents);
static void (*python_handle_error)(void* handle, int revents);
static void (*python_stop)(void* handle);

    struct gevent_ev_io {
        struct ev_io watcher;
        void* handle;
    };
    
    static void _gevent_ev_io_callback(struct ev_loop* loop, struct ev_io* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_io *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_timer {
        struct ev_timer watcher;
        void* handle;
    };
    
    static void _gevent_ev_timer_callback(struct ev_loop* loop, struct ev_timer* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_timer *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_signal {
        struct ev_signal watcher;
        void* handle;
    };
    
    static void _gevent_ev_signal_callback(struct ev_loop* loop, struct ev_signal* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_signal *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_prepare {
        struct ev_prepare watcher;
        void* handle;
    };
    
    static void _gevent_ev_prepare_callback(struct ev_loop* loop, struct ev_prepare* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_prepare *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_check {
        struct ev_check watcher;
        void* handle;
    };
    
    static void _gevent_ev_check_callback(struct ev_loop* loop, struct ev_check* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_check *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_fork {
        struct ev_fork watcher;
        void* handle;
    };
    
    static void _gevent_ev_fork_callback(struct ev_loop* loop, struct ev_fork* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_fork *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_async {
        struct ev_async watcher;
        void* handle;
    };
    
    static void _gevent_ev_async_callback(struct ev_loop* loop, struct ev_async* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_async *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_child {
        struct ev_child watcher;
        void* handle;
    };
    
    static void _gevent_ev_child_callback(struct ev_loop* loop, struct ev_child* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_child *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
    struct gevent_ev_stat {
        struct ev_stat watcher;
        void* handle;
    };
    
    static void _gevent_ev_stat_callback(struct ev_loop* loop, struct ev_stat* watcher, int revents)
    {
        // invoke self.callback()
        void* handle = ((struct gevent_ev_stat *)watcher)->handle;
        if( python_callback(handle, revents) < 0) {
            /* in case of exception, call self.loop.handle_error */
            python_handle_error(handle, revents);
        }
        // Code to stop the event
        if (!ev_is_active(watcher)) {
            python_stop(handle);
        }
    }
    
void _cffi_f__gevent_ev_async_callback(struct ev_loop * x0, struct ev_async * x1, int x2)
{
  _gevent_ev_async_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_check_callback(struct ev_loop * x0, struct ev_check * x1, int x2)
{
  _gevent_ev_check_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_child_callback(struct ev_loop * x0, struct ev_child * x1, int x2)
{
  _gevent_ev_child_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_fork_callback(struct ev_loop * x0, struct ev_fork * x1, int x2)
{
  _gevent_ev_fork_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_io_callback(struct ev_loop * x0, struct ev_io * x1, int x2)
{
  _gevent_ev_io_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_prepare_callback(struct ev_loop * x0, struct ev_prepare * x1, int x2)
{
  _gevent_ev_prepare_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_signal_callback(struct ev_loop * x0, struct ev_signal * x1, int x2)
{
  _gevent_ev_signal_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_stat_callback(struct ev_loop * x0, struct ev_stat * x1, int x2)
{
  _gevent_ev_stat_callback(x0, x1, x2);
}

void _cffi_f__gevent_ev_timer_callback(struct ev_loop * x0, struct ev_timer * x1, int x2)
{
  _gevent_ev_timer_callback(x0, x1, x2);
}

void _cffi_f_ev_async_init(struct ev_async * x0, void * x1)
{
  ev_async_init(x0, x1);
}

int _cffi_f_ev_async_pending(struct ev_async * x0)
{
  return ev_async_pending(x0);
}

void _cffi_f_ev_async_send(struct ev_loop * x0, struct ev_async * x1)
{
  ev_async_send(x0, x1);
}

void _cffi_f_ev_async_start(struct ev_loop * x0, struct ev_async * x1)
{
  ev_async_start(x0, x1);
}

void _cffi_f_ev_async_stop(struct ev_loop * x0, struct ev_async * x1)
{
  ev_async_stop(x0, x1);
}

unsigned int _cffi_f_ev_backend(struct ev_loop * x0)
{
  return ev_backend(x0);
}

void _cffi_f_ev_break(struct ev_loop * x0, int x1)
{
  ev_break(x0, x1);
}

void _cffi_f_ev_check_init(struct ev_check * x0, void * x1)
{
  ev_check_init(x0, x1);
}

void _cffi_f_ev_check_start(struct ev_loop * x0, struct ev_check * x1)
{
  ev_check_start(x0, x1);
}

void _cffi_f_ev_check_stop(struct ev_loop * x0, struct ev_check * x1)
{
  ev_check_stop(x0, x1);
}

void _cffi_f_ev_child_init(struct ev_child * x0, void * x1, int x2, int x3)
{
  ev_child_init(x0, x1, x2, x3);
}

void _cffi_f_ev_child_start(struct ev_loop * x0, struct ev_child * x1)
{
  ev_child_start(x0, x1);
}

void _cffi_f_ev_child_stop(struct ev_loop * x0, struct ev_child * x1)
{
  ev_child_stop(x0, x1);
}

struct ev_loop * _cffi_f_ev_default_loop(unsigned int x0)
{
  return ev_default_loop(x0);
}

unsigned int _cffi_f_ev_depth(struct ev_loop * x0)
{
  return ev_depth(x0);
}

unsigned int _cffi_f_ev_embeddable_backends(void)
{
  return ev_embeddable_backends();
}

void _cffi_f_ev_feed_event(struct ev_loop * x0, void * x1, int x2)
{
  ev_feed_event(x0, x1, x2);
}

void _cffi_f_ev_fork_init(struct ev_fork * x0, void * x1)
{
  ev_fork_init(x0, x1);
}

void _cffi_f_ev_fork_start(struct ev_loop * x0, struct ev_fork * x1)
{
  ev_fork_start(x0, x1);
}

void _cffi_f_ev_fork_stop(struct ev_loop * x0, struct ev_fork * x1)
{
  ev_fork_stop(x0, x1);
}

void _cffi_f_ev_idle_init(struct ev_idle * x0, void * x1)
{
  ev_idle_init(x0, x1);
}

void _cffi_f_ev_idle_start(struct ev_loop * x0, struct ev_idle * x1)
{
  ev_idle_start(x0, x1);
}

void _cffi_f_ev_idle_stop(struct ev_loop * x0, struct ev_idle * x1)
{
  ev_idle_stop(x0, x1);
}

void _cffi_f_ev_io_init(struct ev_io * x0, void * x1, int x2, int x3)
{
  ev_io_init(x0, x1, x2, x3);
}

void _cffi_f_ev_io_start(struct ev_loop * x0, struct ev_io * x1)
{
  ev_io_start(x0, x1);
}

void _cffi_f_ev_io_stop(struct ev_loop * x0, struct ev_io * x1)
{
  ev_io_stop(x0, x1);
}

int _cffi_f_ev_is_active(void * x0)
{
  return ev_is_active(x0);
}

int _cffi_f_ev_is_default_loop(struct ev_loop * x0)
{
  return ev_is_default_loop(x0);
}

int _cffi_f_ev_is_pending(void * x0)
{
  return ev_is_pending(x0);
}

unsigned int _cffi_f_ev_iteration(struct ev_loop * x0)
{
  return ev_iteration(x0);
}

void _cffi_f_ev_loop_destroy(struct ev_loop * x0)
{
  ev_loop_destroy(x0);
}

void _cffi_f_ev_loop_fork(struct ev_loop * x0)
{
  ev_loop_fork(x0);
}

struct ev_loop * _cffi_f_ev_loop_new(unsigned int x0)
{
  return ev_loop_new(x0);
}

double _cffi_f_ev_now(struct ev_loop * x0)
{
  return ev_now(x0);
}

void _cffi_f_ev_now_update(struct ev_loop * x0)
{
  ev_now_update(x0);
}

unsigned int _cffi_f_ev_pending_count(struct ev_loop * x0)
{
  return ev_pending_count(x0);
}

void _cffi_f_ev_prepare_init(struct ev_prepare * x0, void * x1)
{
  ev_prepare_init(x0, x1);
}

void _cffi_f_ev_prepare_start(struct ev_loop * x0, struct ev_prepare * x1)
{
  ev_prepare_start(x0, x1);
}

void _cffi_f_ev_prepare_stop(struct ev_loop * x0, struct ev_prepare * x1)
{
  ev_prepare_stop(x0, x1);
}

int _cffi_f_ev_priority(void * x0)
{
  return ev_priority(x0);
}

unsigned int _cffi_f_ev_recommended_backends(void)
{
  return ev_recommended_backends();
}

void _cffi_f_ev_ref(struct ev_loop * x0)
{
  ev_ref(x0);
}

void _cffi_f_ev_run(struct ev_loop * x0, int x1)
{
  ev_run(x0, x1);
}

void _cffi_f_ev_set_priority(void * x0, int x1)
{
  ev_set_priority(x0, x1);
}

void _cffi_f_ev_set_syserr_cb(void * x0)
{
  ev_set_syserr_cb(x0);
}

void _cffi_f_ev_signal_init(struct ev_signal * x0, void * x1, int x2)
{
  ev_signal_init(x0, x1, x2);
}

void _cffi_f_ev_signal_start(struct ev_loop * x0, struct ev_signal * x1)
{
  ev_signal_start(x0, x1);
}

void _cffi_f_ev_signal_stop(struct ev_loop * x0, struct ev_signal * x1)
{
  ev_signal_stop(x0, x1);
}

void _cffi_f_ev_sleep(double x0)
{
  ev_sleep(x0);
}

void _cffi_f_ev_stat_init(struct ev_stat * x0, void * x1, char * x2, double x3)
{
  ev_stat_init(x0, x1, x2, x3);
}

void _cffi_f_ev_stat_start(struct ev_loop * x0, struct ev_stat * x1)
{
  ev_stat_start(x0, x1);
}

void _cffi_f_ev_stat_stop(struct ev_loop * x0, struct ev_stat * x1)
{
  ev_stat_stop(x0, x1);
}

unsigned int _cffi_f_ev_supported_backends(void)
{
  return ev_supported_backends();
}

double _cffi_f_ev_time(void)
{
  return ev_time();
}

void _cffi_f_ev_timer_again(struct ev_loop * x0, struct ev_timer * x1)
{
  ev_timer_again(x0, x1);
}

void _cffi_f_ev_timer_init(struct ev_timer * x0, void(* x1)(struct ev_loop *, struct ev_timer *, int), double x2, double x3)
{
  ev_timer_init(x0, x1, x2, x3);
}

void _cffi_f_ev_timer_start(struct ev_loop * x0, struct ev_timer * x1)
{
  ev_timer_start(x0, x1);
}

void _cffi_f_ev_timer_stop(struct ev_loop * x0, struct ev_timer * x1)
{
  ev_timer_stop(x0, x1);
}

void _cffi_f_ev_unref(struct ev_loop * x0)
{
  ev_unref(x0);
}

void _cffi_f_ev_verify(struct ev_loop * x0)
{
  ev_verify(x0);
}

int _cffi_f_ev_version_major(void)
{
  return ev_version_major();
}

int _cffi_f_ev_version_minor(void)
{
  return ev_version_minor();
}

struct ev_loop * _cffi_f_gevent_ev_default_loop(unsigned int x0)
{
  return gevent_ev_default_loop(x0);
}

void _cffi_f_gevent_install_sigchld_handler(void)
{
  gevent_install_sigchld_handler();
}

int _cffi_const_EVBACKEND_ALL(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_ALL);
  return (EVBACKEND_ALL) <= 0;
}

int _cffi_const_EVBACKEND_DEVPOLL(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_DEVPOLL);
  return (EVBACKEND_DEVPOLL) <= 0;
}

int _cffi_const_EVBACKEND_EPOLL(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_EPOLL);
  return (EVBACKEND_EPOLL) <= 0;
}

int _cffi_const_EVBACKEND_KQUEUE(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_KQUEUE);
  return (EVBACKEND_KQUEUE) <= 0;
}

int _cffi_const_EVBACKEND_MASK(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_MASK);
  return (EVBACKEND_MASK) <= 0;
}

int _cffi_const_EVBACKEND_POLL(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_POLL);
  return (EVBACKEND_POLL) <= 0;
}

int _cffi_const_EVBACKEND_PORT(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_PORT);
  return (EVBACKEND_PORT) <= 0;
}

int _cffi_const_EVBACKEND_SELECT(long long *out_value)
{
  *out_value = (long long)(EVBACKEND_SELECT);
  return (EVBACKEND_SELECT) <= 0;
}

int _cffi_const_EVBREAK_ALL(long long *out_value)
{
  *out_value = (long long)(EVBREAK_ALL);
  return (EVBREAK_ALL) <= 0;
}

int _cffi_const_EVBREAK_CANCEL(long long *out_value)
{
  *out_value = (long long)(EVBREAK_CANCEL);
  return (EVBREAK_CANCEL) <= 0;
}

int _cffi_const_EVBREAK_ONE(long long *out_value)
{
  *out_value = (long long)(EVBREAK_ONE);
  return (EVBREAK_ONE) <= 0;
}

int _cffi_const_EVFLAG_AUTO(long long *out_value)
{
  *out_value = (long long)(EVFLAG_AUTO);
  return (EVFLAG_AUTO) <= 0;
}

int _cffi_const_EVFLAG_FORKCHECK(long long *out_value)
{
  *out_value = (long long)(EVFLAG_FORKCHECK);
  return (EVFLAG_FORKCHECK) <= 0;
}

int _cffi_const_EVFLAG_NOENV(long long *out_value)
{
  *out_value = (long long)(EVFLAG_NOENV);
  return (EVFLAG_NOENV) <= 0;
}

int _cffi_const_EVFLAG_NOINOTIFY(long long *out_value)
{
  *out_value = (long long)(EVFLAG_NOINOTIFY);
  return (EVFLAG_NOINOTIFY) <= 0;
}

int _cffi_const_EVFLAG_NOSIGMASK(long long *out_value)
{
  *out_value = (long long)(EVFLAG_NOSIGMASK);
  return (EVFLAG_NOSIGMASK) <= 0;
}

int _cffi_const_EVFLAG_SIGNALFD(long long *out_value)
{
  *out_value = (long long)(EVFLAG_SIGNALFD);
  return (EVFLAG_SIGNALFD) <= 0;
}

int _cffi_const_EVRUN_NOWAIT(long long *out_value)
{
  *out_value = (long long)(EVRUN_NOWAIT);
  return (EVRUN_NOWAIT) <= 0;
}

int _cffi_const_EVRUN_ONCE(long long *out_value)
{
  *out_value = (long long)(EVRUN_ONCE);
  return (EVRUN_ONCE) <= 0;
}

int _cffi_const_EV_ASYNC(long long *out_value)
{
  *out_value = (long long)(EV_ASYNC);
  return (EV_ASYNC) <= 0;
}

int _cffi_const_EV_CHECK(long long *out_value)
{
  *out_value = (long long)(EV_CHECK);
  return (EV_CHECK) <= 0;
}

int _cffi_const_EV_CHILD(long long *out_value)
{
  *out_value = (long long)(EV_CHILD);
  return (EV_CHILD) <= 0;
}

int _cffi_const_EV_CLEANUP(long long *out_value)
{
  *out_value = (long long)(EV_CLEANUP);
  return (EV_CLEANUP) <= 0;
}

int _cffi_const_EV_CUSTOM(long long *out_value)
{
  *out_value = (long long)(EV_CUSTOM);
  return (EV_CUSTOM) <= 0;
}

int _cffi_const_EV_EMBED(long long *out_value)
{
  *out_value = (long long)(EV_EMBED);
  return (EV_EMBED) <= 0;
}

int _cffi_const_EV_ERROR(long long *out_value)
{
  *out_value = (long long)(EV_ERROR);
  return (EV_ERROR) <= 0;
}

int _cffi_const_EV_FORK(long long *out_value)
{
  *out_value = (long long)(EV_FORK);
  return (EV_FORK) <= 0;
}

int _cffi_const_EV_IDLE(long long *out_value)
{
  *out_value = (long long)(EV_IDLE);
  return (EV_IDLE) <= 0;
}

int _cffi_const_EV_MAXPRI(long long *out_value)
{
  *out_value = (long long)(EV_MAXPRI);
  return (EV_MAXPRI) <= 0;
}

int _cffi_const_EV_MINPRI(long long *out_value)
{
  *out_value = (long long)(EV_MINPRI);
  return (EV_MINPRI) <= 0;
}

int _cffi_const_EV_NONE(long long *out_value)
{
  *out_value = (long long)(EV_NONE);
  return (EV_NONE) <= 0;
}

int _cffi_const_EV_PERIODIC(long long *out_value)
{
  *out_value = (long long)(EV_PERIODIC);
  return (EV_PERIODIC) <= 0;
}

int _cffi_const_EV_PREPARE(long long *out_value)
{
  *out_value = (long long)(EV_PREPARE);
  return (EV_PREPARE) <= 0;
}

int _cffi_const_EV_READ(long long *out_value)
{
  *out_value = (long long)(EV_READ);
  return (EV_READ) <= 0;
}

int _cffi_const_EV_SIGNAL(long long *out_value)
{
  *out_value = (long long)(EV_SIGNAL);
  return (EV_SIGNAL) <= 0;
}

int _cffi_const_EV_STAT(long long *out_value)
{
  *out_value = (long long)(EV_STAT);
  return (EV_STAT) <= 0;
}

int _cffi_const_EV_TIMER(long long *out_value)
{
  *out_value = (long long)(EV_TIMER);
  return (EV_TIMER) <= 0;
}

int _cffi_const_EV_UNDEF(long long *out_value)
{
  *out_value = (long long)(EV_UNDEF);
  return (EV_UNDEF) <= 0;
}

int _cffi_const_EV_VERSION_MAJOR(long long *out_value)
{
  *out_value = (long long)(EV_VERSION_MAJOR);
  return (EV_VERSION_MAJOR) <= 0;
}

int _cffi_const_EV_VERSION_MINOR(long long *out_value)
{
  *out_value = (long long)(EV_VERSION_MINOR);
  return (EV_VERSION_MINOR) <= 0;
}

int _cffi_const_EV_WRITE(long long *out_value)
{
  *out_value = (long long)(EV_WRITE);
  return (EV_WRITE) <= 0;
}

int _cffi_const_EV__IOFDSET(long long *out_value)
{
  *out_value = (long long)(EV__IOFDSET);
  return (EV__IOFDSET) <= 0;
}

static void _cffi_check_struct_ev_async(struct ev_async *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
}
intptr_t _cffi_layout_struct_ev_async(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_async y; };
  static intptr_t nums[] = {
    sizeof(struct ev_async),
    offsetof(struct _cffi_aligncheck, y),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_async(0);
}

static void _cffi_check_struct_ev_check(struct ev_check *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
}
intptr_t _cffi_layout_struct_ev_check(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_check y; };
  static intptr_t nums[] = {
    sizeof(struct ev_check),
    offsetof(struct _cffi_aligncheck, y),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_check(0);
}

static void _cffi_check_struct_ev_child(struct ev_child *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  (void)((p->pid) << 1);
  (void)((p->rpid) << 1);
  (void)((p->rstatus) << 1);
}
intptr_t _cffi_layout_struct_ev_child(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_child y; };
  static intptr_t nums[] = {
    sizeof(struct ev_child),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct ev_child, pid),
    sizeof(((struct ev_child *)0)->pid),
    offsetof(struct ev_child, rpid),
    sizeof(((struct ev_child *)0)->rpid),
    offsetof(struct ev_child, rstatus),
    sizeof(((struct ev_child *)0)->rstatus),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_child(0);
}

static void _cffi_check_struct_ev_fork(struct ev_fork *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
}
intptr_t _cffi_layout_struct_ev_fork(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_fork y; };
  static intptr_t nums[] = {
    sizeof(struct ev_fork),
    offsetof(struct _cffi_aligncheck, y),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_fork(0);
}

static void _cffi_check_struct_ev_idle(struct ev_idle *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
}
intptr_t _cffi_layout_struct_ev_idle(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_idle y; };
  static intptr_t nums[] = {
    sizeof(struct ev_idle),
    offsetof(struct _cffi_aligncheck, y),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_idle(0);
}

static void _cffi_check_struct_ev_io(struct ev_io *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  (void)((p->fd) << 1);
  (void)((p->events) << 1);
}
intptr_t _cffi_layout_struct_ev_io(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_io y; };
  static intptr_t nums[] = {
    sizeof(struct ev_io),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct ev_io, fd),
    sizeof(((struct ev_io *)0)->fd),
    offsetof(struct ev_io, events),
    sizeof(((struct ev_io *)0)->events),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_io(0);
}

static void _cffi_check_struct_ev_loop(struct ev_loop *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  (void)((p->backend_fd) << 1);
  (void)((p->activecnt) << 1);
}
intptr_t _cffi_layout_struct_ev_loop(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_loop y; };
  static intptr_t nums[] = {
    sizeof(struct ev_loop),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct ev_loop, backend_fd),
    sizeof(((struct ev_loop *)0)->backend_fd),
    offsetof(struct ev_loop, activecnt),
    sizeof(((struct ev_loop *)0)->activecnt),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_loop(0);
}

static void _cffi_check_struct_ev_prepare(struct ev_prepare *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
}
intptr_t _cffi_layout_struct_ev_prepare(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_prepare y; };
  static intptr_t nums[] = {
    sizeof(struct ev_prepare),
    offsetof(struct _cffi_aligncheck, y),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_prepare(0);
}

static void _cffi_check_struct_ev_signal(struct ev_signal *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
}
intptr_t _cffi_layout_struct_ev_signal(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_signal y; };
  static intptr_t nums[] = {
    sizeof(struct ev_signal),
    offsetof(struct _cffi_aligncheck, y),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_signal(0);
}

static void _cffi_check_struct_ev_stat(struct ev_stat *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct stat *tmp = &p->attr; (void)tmp; }
  { char const * *tmp = &p->path; (void)tmp; }
  { struct stat *tmp = &p->prev; (void)tmp; }
  { double *tmp = &p->interval; (void)tmp; }
}
intptr_t _cffi_layout_struct_ev_stat(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_stat y; };
  static intptr_t nums[] = {
    sizeof(struct ev_stat),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct ev_stat, attr),
    sizeof(((struct ev_stat *)0)->attr),
    offsetof(struct ev_stat, path),
    sizeof(((struct ev_stat *)0)->path),
    offsetof(struct ev_stat, prev),
    sizeof(((struct ev_stat *)0)->prev),
    offsetof(struct ev_stat, interval),
    sizeof(((struct ev_stat *)0)->interval),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_stat(0);
}

static void _cffi_check_struct_ev_timer(struct ev_timer *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { double *tmp = &p->at; (void)tmp; }
}
intptr_t _cffi_layout_struct_ev_timer(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct ev_timer y; };
  static intptr_t nums[] = {
    sizeof(struct ev_timer),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct ev_timer, at),
    sizeof(((struct ev_timer *)0)->at),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ev_timer(0);
}

static void _cffi_check_struct_gevent_ev_async(struct gevent_ev_async *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_async *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_async(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_async y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_async),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_async, watcher),
    sizeof(((struct gevent_ev_async *)0)->watcher),
    offsetof(struct gevent_ev_async, handle),
    sizeof(((struct gevent_ev_async *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_async(0);
}

static void _cffi_check_struct_gevent_ev_check(struct gevent_ev_check *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_check *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_check(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_check y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_check),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_check, watcher),
    sizeof(((struct gevent_ev_check *)0)->watcher),
    offsetof(struct gevent_ev_check, handle),
    sizeof(((struct gevent_ev_check *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_check(0);
}

static void _cffi_check_struct_gevent_ev_child(struct gevent_ev_child *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_child *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_child(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_child y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_child),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_child, watcher),
    sizeof(((struct gevent_ev_child *)0)->watcher),
    offsetof(struct gevent_ev_child, handle),
    sizeof(((struct gevent_ev_child *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_child(0);
}

static void _cffi_check_struct_gevent_ev_fork(struct gevent_ev_fork *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_fork *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_fork(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_fork y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_fork),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_fork, watcher),
    sizeof(((struct gevent_ev_fork *)0)->watcher),
    offsetof(struct gevent_ev_fork, handle),
    sizeof(((struct gevent_ev_fork *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_fork(0);
}

static void _cffi_check_struct_gevent_ev_io(struct gevent_ev_io *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_io *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_io(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_io y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_io),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_io, watcher),
    sizeof(((struct gevent_ev_io *)0)->watcher),
    offsetof(struct gevent_ev_io, handle),
    sizeof(((struct gevent_ev_io *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_io(0);
}

static void _cffi_check_struct_gevent_ev_prepare(struct gevent_ev_prepare *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_prepare *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_prepare(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_prepare y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_prepare),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_prepare, watcher),
    sizeof(((struct gevent_ev_prepare *)0)->watcher),
    offsetof(struct gevent_ev_prepare, handle),
    sizeof(((struct gevent_ev_prepare *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_prepare(0);
}

static void _cffi_check_struct_gevent_ev_signal(struct gevent_ev_signal *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_signal *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_signal(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_signal y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_signal),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_signal, watcher),
    sizeof(((struct gevent_ev_signal *)0)->watcher),
    offsetof(struct gevent_ev_signal, handle),
    sizeof(((struct gevent_ev_signal *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_signal(0);
}

static void _cffi_check_struct_gevent_ev_stat(struct gevent_ev_stat *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_stat *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_stat(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_stat y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_stat),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_stat, watcher),
    sizeof(((struct gevent_ev_stat *)0)->watcher),
    offsetof(struct gevent_ev_stat, handle),
    sizeof(((struct gevent_ev_stat *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_stat(0);
}

static void _cffi_check_struct_gevent_ev_timer(struct gevent_ev_timer *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  { struct ev_timer *tmp = &p->watcher; (void)tmp; }
  { void * *tmp = &p->handle; (void)tmp; }
}
intptr_t _cffi_layout_struct_gevent_ev_timer(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct gevent_ev_timer y; };
  static intptr_t nums[] = {
    sizeof(struct gevent_ev_timer),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct gevent_ev_timer, watcher),
    sizeof(((struct gevent_ev_timer *)0)->watcher),
    offsetof(struct gevent_ev_timer, handle),
    sizeof(((struct gevent_ev_timer *)0)->handle),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_gevent_ev_timer(0);
}

static void _cffi_check_struct_stat(struct stat *p)
{
  /* only to generate compile-time warnings or errors */
  (void)p;
  (void)((p->st_nlink) << 1);
}
intptr_t _cffi_layout_struct_stat(intptr_t i)
{
  struct _cffi_aligncheck { char x; struct stat y; };
  static intptr_t nums[] = {
    sizeof(struct stat),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct stat, st_nlink),
    sizeof(((struct stat *)0)->st_nlink),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_stat(0);
}

void(* * _cffi_var_gevent_noop(void))(struct ev_loop *, struct ev_timer *, int)
{
  return (&gevent_noop);
}

int(* * _cffi_var_python_callback(void))(void *, int)
{
  return (&python_callback);
}

void(* * _cffi_var_python_handle_error(void))(void *, int)
{
  return (&python_handle_error);
}

void(* * _cffi_var_python_stop(void))(void *)
{
  return (&python_stop);
}

