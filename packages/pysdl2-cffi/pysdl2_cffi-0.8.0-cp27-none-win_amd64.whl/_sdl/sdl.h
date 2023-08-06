extern const char * SDL_GetPlatform (void);
typedef unsigned char uint8_t;
typedef unsigned short int uint16_t;
typedef unsigned int uint32_t;
typedef unsigned long int uint64_t;
typedef signed char int_least8_t;
typedef short int int_least16_t;
typedef int int_least32_t;
typedef long int int_least64_t;
typedef unsigned char uint_least8_t;
typedef unsigned short int uint_least16_t;
typedef unsigned int uint_least32_t;
typedef unsigned long int uint_least64_t;
typedef signed char int_fast8_t;
typedef long int int_fast16_t;
typedef long int int_fast32_t;
typedef long int int_fast64_t;
typedef unsigned char uint_fast8_t;
typedef unsigned long int uint_fast16_t;
typedef unsigned long int uint_fast32_t;
typedef unsigned long int uint_fast64_t;
typedef long int intptr_t;
typedef unsigned long int uintptr_t;
typedef long int intmax_t;
typedef unsigned long int uintmax_t;
typedef enum
{
    SDL_FALSE = 0,
    SDL_TRUE = 1
} SDL_bool;
typedef int8_t Sint8;
typedef uint8_t Uint8;
typedef int16_t Sint16;
typedef uint16_t Uint16;
typedef int32_t Sint32;
typedef uint32_t Uint32;
typedef int64_t Sint64;
typedef uint64_t Uint64;
extern void * SDL_malloc(size_t size);
extern void * SDL_calloc(size_t nmemb, size_t size);
extern void * SDL_realloc(void *mem, size_t size);
extern void SDL_free(void *mem);
extern char * SDL_getenv(const char *name);
extern int SDL_setenv(const char *name, const char *value, int overwrite);
extern void SDL_qsort(void *base, size_t nmemb, size_t size, int (*compare) (const void *, const void *));
extern int SDL_abs(int x);
extern int SDL_isdigit(int x);
extern int SDL_isspace(int x);
extern int SDL_toupper(int x);
extern int SDL_tolower(int x);
extern void * SDL_memset(void *dst, int c, size_t len);
extern void * SDL_memcpy(void *dst, const void *src, size_t len);
extern void * SDL_memmove(void *dst, const void *src, size_t len);
extern int SDL_memcmp(const void *s1, const void *s2, size_t len);
extern size_t SDL_wcslen(const wchar_t *wstr);
extern size_t SDL_wcslcpy(wchar_t *dst, const wchar_t *src, size_t maxlen);
extern size_t SDL_wcslcat(wchar_t *dst, const wchar_t *src, size_t maxlen);
extern size_t SDL_strlen(const char *str);
extern size_t SDL_strlcpy(char *dst, const char *src, size_t maxlen);
extern size_t SDL_utf8strlcpy(char *dst, const char *src, size_t dst_bytes);
extern size_t SDL_strlcat(char *dst, const char *src, size_t maxlen);
extern char * SDL_strdup(const char *str);
extern char * SDL_strrev(char *str);
extern char * SDL_strupr(char *str);
extern char * SDL_strlwr(char *str);
extern char * SDL_strchr(const char *str, int c);
extern char * SDL_strrchr(const char *str, int c);
extern char * SDL_strstr(const char *haystack, const char *needle);
extern char * SDL_itoa(int value, char *str, int radix);
extern char * SDL_uitoa(unsigned int value, char *str, int radix);
extern char * SDL_ltoa(long value, char *str, int radix);
extern char * SDL_ultoa(unsigned long value, char *str, int radix);
extern char * SDL_lltoa(Sint64 value, char *str, int radix);
extern char * SDL_ulltoa(Uint64 value, char *str, int radix);
extern int SDL_atoi(const char *str);
extern double SDL_atof(const char *str);
extern long SDL_strtol(const char *str, char **endp, int base);
extern unsigned long SDL_strtoul(const char *str, char **endp, int base);
extern Sint64 SDL_strtoll(const char *str, char **endp, int base);
extern Uint64 SDL_strtoull(const char *str, char **endp, int base);
extern double SDL_strtod(const char *str, char **endp);
extern int SDL_strcmp(const char *str1, const char *str2);
extern int SDL_strncmp(const char *str1, const char *str2, size_t maxlen);
extern int SDL_strcasecmp(const char *str1, const char *str2);
extern int SDL_strncasecmp(const char *str1, const char *str2, size_t len);
extern int SDL_sscanf(const char *text, const char *fmt, ...);
extern int SDL_snprintf(char *text, size_t maxlen, const char *fmt, ...);
extern double SDL_acos(double x);
extern double SDL_asin(double x);
extern double SDL_atan(double x);
extern double SDL_atan2(double x, double y);
extern double SDL_ceil(double x);
extern double SDL_copysign(double x, double y);
extern double SDL_cos(double x);
extern float SDL_cosf(float x);
extern double SDL_fabs(double x);
extern double SDL_floor(double x);
extern double SDL_log(double x);
extern double SDL_pow(double x, double y);
extern double SDL_scalbn(double x, int n);
extern double SDL_sin(double x);
extern float SDL_sinf(float x);
extern double SDL_sqrt(double x);
typedef struct _SDL_iconv_t *SDL_iconv_t;
extern SDL_iconv_t SDL_iconv_open(const char *tocode,
                                                   const char *fromcode);
extern int SDL_iconv_close(SDL_iconv_t cd);
extern size_t SDL_iconv(SDL_iconv_t cd, const char **inbuf,
                                         size_t * inbytesleft, char **outbuf,
                                         size_t * outbytesleft);
extern char * SDL_iconv_string(const char *tocode,
                                               const char *fromcode,
                                               const char *inbuf,
                                               size_t inbytesleft);
extern void SDL_SetMainReady(void);
typedef enum
{
    SDL_ASSERTION_RETRY,
    SDL_ASSERTION_BREAK,
    SDL_ASSERTION_ABORT,
    SDL_ASSERTION_IGNORE,
    SDL_ASSERTION_ALWAYS_IGNORE
} SDL_assert_state;
typedef struct SDL_assert_data
{
    int always_ignore;
    unsigned int trigger_count;
    const char *condition;
    const char *filename;
    int linenum;
    const char *function;
    const struct SDL_assert_data *next;
} SDL_assert_data;
extern SDL_assert_state SDL_ReportAssertion(SDL_assert_data *,
                                                             const char *,
                                                             const char *, int)
;
typedef SDL_assert_state ( *SDL_AssertionHandler)(
                                 const SDL_assert_data* data, void* userdata);
extern void SDL_SetAssertionHandler(
                                            SDL_AssertionHandler handler,
                                            void *userdata);
extern SDL_AssertionHandler SDL_GetDefaultAssertionHandler(void);
extern SDL_AssertionHandler SDL_GetAssertionHandler(void **puserdata);
extern const SDL_assert_data * SDL_GetAssertionReport(void);
extern void SDL_ResetAssertionReport(void);
typedef int SDL_SpinLock;
extern SDL_bool SDL_AtomicTryLock(SDL_SpinLock *lock);
extern void SDL_AtomicLock(SDL_SpinLock *lock);
extern void SDL_AtomicUnlock(SDL_SpinLock *lock);
typedef struct { int value; } SDL_atomic_t;
extern SDL_bool SDL_AtomicCAS(SDL_atomic_t *a, int oldval, int newval);
extern int SDL_AtomicSet(SDL_atomic_t *a, int v);
extern int SDL_AtomicGet(SDL_atomic_t *a);
extern int SDL_AtomicAdd(SDL_atomic_t *a, int v);
extern SDL_bool SDL_AtomicCASPtr(void **a, void *oldval, void *newval);
extern void* SDL_AtomicSetPtr(void **a, void* v);
extern void* SDL_AtomicGetPtr(void **a);
extern int SDL_SetError(const char *fmt, ...);
extern const char * SDL_GetError(void);
extern void SDL_ClearError(void);
typedef enum
{
    SDL_ENOMEM,
    SDL_EFREAD,
    SDL_EFWRITE,
    SDL_EFSEEK,
    SDL_UNSUPPORTED,
    SDL_LASTERROR
} SDL_errorcode;
extern int SDL_Error(SDL_errorcode code);
struct SDL_mutex;
typedef struct SDL_mutex SDL_mutex;
extern SDL_mutex * SDL_CreateMutex(void);
extern int SDL_LockMutex(SDL_mutex * mutex);
extern int SDL_TryLockMutex(SDL_mutex * mutex);
extern int SDL_UnlockMutex(SDL_mutex * mutex);
extern void SDL_DestroyMutex(SDL_mutex * mutex);
struct SDL_semaphore;
typedef struct SDL_semaphore SDL_sem;
extern SDL_sem * SDL_CreateSemaphore(Uint32 initial_value);
extern void SDL_DestroySemaphore(SDL_sem * sem);
extern int SDL_SemWait(SDL_sem * sem);
extern int SDL_SemTryWait(SDL_sem * sem);
extern int SDL_SemWaitTimeout(SDL_sem * sem, Uint32 ms);
extern int SDL_SemPost(SDL_sem * sem);
extern Uint32 SDL_SemValue(SDL_sem * sem);
struct SDL_cond;
typedef struct SDL_cond SDL_cond;
extern SDL_cond * SDL_CreateCond(void);
extern void SDL_DestroyCond(SDL_cond * cond);
extern int SDL_CondSignal(SDL_cond * cond);
extern int SDL_CondBroadcast(SDL_cond * cond);
extern int SDL_CondWait(SDL_cond * cond, SDL_mutex * mutex);
extern int SDL_CondWaitTimeout(SDL_cond * cond,
                                                SDL_mutex * mutex, Uint32 ms);
struct SDL_Thread;
typedef struct SDL_Thread SDL_Thread;
typedef unsigned long SDL_threadID;
typedef unsigned int SDL_TLSID;
typedef enum {
    SDL_THREAD_PRIORITY_LOW,
    SDL_THREAD_PRIORITY_NORMAL,
    SDL_THREAD_PRIORITY_HIGH
} SDL_ThreadPriority;
typedef int ( * SDL_ThreadFunction) (void *data);
extern SDL_Thread *
SDL_CreateThread(SDL_ThreadFunction fn, const char *name, void *data);
extern const char * SDL_GetThreadName(SDL_Thread *thread);
extern SDL_threadID SDL_ThreadID(void);
extern SDL_threadID SDL_GetThreadID(SDL_Thread * thread);
extern int SDL_SetThreadPriority(SDL_ThreadPriority priority);
extern void SDL_WaitThread(SDL_Thread * thread, int *status);
extern void SDL_DetachThread(SDL_Thread * thread);
extern SDL_TLSID SDL_TLSCreate(void);
extern void * SDL_TLSGet(SDL_TLSID id);
extern int SDL_TLSSet(SDL_TLSID id, const void *value, void (*destructor)(void*));
typedef struct SDL_RWops
{
    Sint64 ( * size) (struct SDL_RWops * context);
    Sint64 ( * seek) (struct SDL_RWops * context, Sint64 offset,
                             int whence);
    size_t ( * read) (struct SDL_RWops * context, void *ptr,
                             size_t size, size_t maxnum);
    size_t ( * write) (struct SDL_RWops * context, const void *ptr,
                              size_t size, size_t num);
    int ( * close) (struct SDL_RWops * context);
    Uint32 type;
    union
    {
        struct
        {
            SDL_bool autoclose;
            FILE *fp;
        } stdio;
        struct
        {
            Uint8 *base;
            Uint8 *here;
            Uint8 *stop;
        } mem;
        struct
        {
            void *data1;
            void *data2;
        } unknown;
    } hidden;
} SDL_RWops;
extern SDL_RWops * SDL_RWFromFile(const char *file,
                                                  const char *mode);
extern SDL_RWops * SDL_RWFromFP(FILE * fp,
                                                SDL_bool autoclose);
extern SDL_RWops * SDL_RWFromMem(void *mem, int size);
extern SDL_RWops * SDL_RWFromConstMem(const void *mem,
                                                      int size);
extern SDL_RWops * SDL_AllocRW(void);
extern void SDL_FreeRW(SDL_RWops * area);
extern Uint8 SDL_ReadU8(SDL_RWops * src);
extern Uint16 SDL_ReadLE16(SDL_RWops * src);
extern Uint16 SDL_ReadBE16(SDL_RWops * src);
extern Uint32 SDL_ReadLE32(SDL_RWops * src);
extern Uint32 SDL_ReadBE32(SDL_RWops * src);
extern Uint64 SDL_ReadLE64(SDL_RWops * src);
extern Uint64 SDL_ReadBE64(SDL_RWops * src);
extern size_t SDL_WriteU8(SDL_RWops * dst, Uint8 value);
extern size_t SDL_WriteLE16(SDL_RWops * dst, Uint16 value);
extern size_t SDL_WriteBE16(SDL_RWops * dst, Uint16 value);
extern size_t SDL_WriteLE32(SDL_RWops * dst, Uint32 value);
extern size_t SDL_WriteBE32(SDL_RWops * dst, Uint32 value);
extern size_t SDL_WriteLE64(SDL_RWops * dst, Uint64 value);
extern size_t SDL_WriteBE64(SDL_RWops * dst, Uint64 value);
typedef Uint16 SDL_AudioFormat;
typedef void ( * SDL_AudioCallback) (void *userdata, Uint8 * stream,
                                            int len);
typedef struct SDL_AudioSpec
{
    int freq;
    SDL_AudioFormat format;
    Uint8 channels;
    Uint8 silence;
    Uint16 samples;
    Uint16 padding;
    Uint32 size;
    SDL_AudioCallback callback;
    void *userdata;
} SDL_AudioSpec;
struct SDL_AudioCVT;
typedef void ( * SDL_AudioFilter) (struct SDL_AudioCVT * cvt,
                                          SDL_AudioFormat format);
typedef struct SDL_AudioCVT
{
    int needed;
    SDL_AudioFormat src_format;
    SDL_AudioFormat dst_format;
    double rate_incr;
    Uint8 *buf;
    int len;
    int len_cvt;
    int len_mult;
    double len_ratio;
    SDL_AudioFilter filters[10];
    int filter_index;
}  SDL_AudioCVT;
extern int SDL_GetNumAudioDrivers(void);
extern const char * SDL_GetAudioDriver(int index);
extern int SDL_AudioInit(const char *driver_name);
extern void SDL_AudioQuit(void);
extern const char * SDL_GetCurrentAudioDriver(void);
extern int SDL_OpenAudio(SDL_AudioSpec * desired,
                                          SDL_AudioSpec * obtained);
typedef Uint32 SDL_AudioDeviceID;
extern int SDL_GetNumAudioDevices(int iscapture);
extern const char * SDL_GetAudioDeviceName(int index,
                                                           int iscapture);
extern SDL_AudioDeviceID SDL_OpenAudioDevice(const char
                                                              *device,
                                                              int iscapture,
                                                              const
                                                              SDL_AudioSpec *
                                                              desired,
                                                              SDL_AudioSpec *
                                                              obtained,
                                                              int
                                                              allowed_changes);
typedef enum
{
    SDL_AUDIO_STOPPED = 0,
    SDL_AUDIO_PLAYING,
    SDL_AUDIO_PAUSED
} SDL_AudioStatus;
extern SDL_AudioStatus SDL_GetAudioStatus(void);
extern SDL_AudioStatus
SDL_GetAudioDeviceStatus(SDL_AudioDeviceID dev);
extern void SDL_PauseAudio(int pause_on);
extern void SDL_PauseAudioDevice(SDL_AudioDeviceID dev,
                                                  int pause_on);
extern SDL_AudioSpec * SDL_LoadWAV_RW(SDL_RWops * src,
                                                      int freesrc,
                                                      SDL_AudioSpec * spec,
                                                      Uint8 ** audio_buf,
                                                      Uint32 * audio_len);
extern void SDL_FreeWAV(Uint8 * audio_buf);
extern int SDL_BuildAudioCVT(SDL_AudioCVT * cvt,
                                              SDL_AudioFormat src_format,
                                              Uint8 src_channels,
                                              int src_rate,
                                              SDL_AudioFormat dst_format,
                                              Uint8 dst_channels,
                                              int dst_rate);
extern int SDL_ConvertAudio(SDL_AudioCVT * cvt);
extern void SDL_MixAudio(Uint8 * dst, const Uint8 * src,
                                          Uint32 len, int volume);
extern void SDL_MixAudioFormat(Uint8 * dst,
                                                const Uint8 * src,
                                                SDL_AudioFormat format,
                                                Uint32 len, int volume);
extern void SDL_LockAudio(void);
extern void SDL_LockAudioDevice(SDL_AudioDeviceID dev);
extern void SDL_UnlockAudio(void);
extern void SDL_UnlockAudioDevice(SDL_AudioDeviceID dev);
extern void SDL_CloseAudio(void);
extern void SDL_CloseAudioDevice(SDL_AudioDeviceID dev);
extern int SDL_SetClipboardText(const char *text);
extern char * SDL_GetClipboardText(void);
extern SDL_bool SDL_HasClipboardText(void);
extern int SDL_GetCPUCount(void);
extern int SDL_GetCPUCacheLineSize(void);
extern SDL_bool SDL_HasRDTSC(void);
extern SDL_bool SDL_HasAltiVec(void);
extern SDL_bool SDL_HasMMX(void);
extern SDL_bool SDL_Has3DNow(void);
extern SDL_bool SDL_HasSSE(void);
extern SDL_bool SDL_HasSSE2(void);
extern SDL_bool SDL_HasSSE3(void);
extern SDL_bool SDL_HasSSE41(void);
extern SDL_bool SDL_HasSSE42(void);
extern SDL_bool SDL_HasAVX(void);
extern int SDL_GetSystemRAM(void);
enum
{
    SDL_PIXELTYPE_UNKNOWN,
    SDL_PIXELTYPE_INDEX1,
    SDL_PIXELTYPE_INDEX4,
    SDL_PIXELTYPE_INDEX8,
    SDL_PIXELTYPE_PACKED8,
    SDL_PIXELTYPE_PACKED16,
    SDL_PIXELTYPE_PACKED32,
    SDL_PIXELTYPE_ARRAYU8,
    SDL_PIXELTYPE_ARRAYU16,
    SDL_PIXELTYPE_ARRAYU32,
    SDL_PIXELTYPE_ARRAYF16,
    SDL_PIXELTYPE_ARRAYF32
};
enum
{
    SDL_BITMAPORDER_NONE,
    SDL_BITMAPORDER_4321,
    SDL_BITMAPORDER_1234
};
enum
{
    SDL_PACKEDORDER_NONE,
    SDL_PACKEDORDER_XRGB,
    SDL_PACKEDORDER_RGBX,
    SDL_PACKEDORDER_ARGB,
    SDL_PACKEDORDER_RGBA,
    SDL_PACKEDORDER_XBGR,
    SDL_PACKEDORDER_BGRX,
    SDL_PACKEDORDER_ABGR,
    SDL_PACKEDORDER_BGRA
};
enum
{
    SDL_ARRAYORDER_NONE,
    SDL_ARRAYORDER_RGB,
    SDL_ARRAYORDER_RGBA,
    SDL_ARRAYORDER_ARGB,
    SDL_ARRAYORDER_BGR,
    SDL_ARRAYORDER_BGRA,
    SDL_ARRAYORDER_ABGR
};
enum
{
    SDL_PACKEDLAYOUT_NONE,
    SDL_PACKEDLAYOUT_332,
    SDL_PACKEDLAYOUT_4444,
    SDL_PACKEDLAYOUT_1555,
    SDL_PACKEDLAYOUT_5551,
    SDL_PACKEDLAYOUT_565,
    SDL_PACKEDLAYOUT_8888,
    SDL_PACKEDLAYOUT_2101010,
    SDL_PACKEDLAYOUT_1010102
};
enum
{
    SDL_PIXELFORMAT_UNKNOWN,
    SDL_PIXELFORMAT_INDEX1LSB = ...  ,
    SDL_PIXELFORMAT_INDEX1MSB = ...  ,
    SDL_PIXELFORMAT_INDEX4LSB = ...  ,
    SDL_PIXELFORMAT_INDEX4MSB = ...  ,
    SDL_PIXELFORMAT_INDEX8 = ... ,
    SDL_PIXELFORMAT_RGB332 = ... ,
    SDL_PIXELFORMAT_RGB444 = ... ,
    SDL_PIXELFORMAT_RGB555 = ... ,
    SDL_PIXELFORMAT_BGR555 = ...  ,
    SDL_PIXELFORMAT_ARGB4444 = ...  ,
    SDL_PIXELFORMAT_RGBA4444 = ...  ,
    SDL_PIXELFORMAT_ABGR4444 = ...  ,
    SDL_PIXELFORMAT_BGRA4444 = ...  ,
    SDL_PIXELFORMAT_ARGB1555 = ...  ,
    SDL_PIXELFORMAT_RGBA5551 = ...  ,
    SDL_PIXELFORMAT_ABGR1555 = ...  ,
    SDL_PIXELFORMAT_BGRA5551 = ...  ,
    SDL_PIXELFORMAT_RGB565 = ...  ,
    SDL_PIXELFORMAT_BGR565 = ...  ,
    SDL_PIXELFORMAT_RGB24 = ...  ,
    SDL_PIXELFORMAT_BGR24 = ...  ,
    SDL_PIXELFORMAT_RGB888 = ...  ,
    SDL_PIXELFORMAT_RGBX8888 = ...  ,
    SDL_PIXELFORMAT_BGR888 = ...  ,
    SDL_PIXELFORMAT_BGRX8888 = ...  ,
    SDL_PIXELFORMAT_ARGB8888 = ...  ,
    SDL_PIXELFORMAT_RGBA8888 = ...  ,
    SDL_PIXELFORMAT_ABGR8888 = ...  ,
    SDL_PIXELFORMAT_BGRA8888 = ...  ,
    SDL_PIXELFORMAT_ARGB2101010 = ...  ,
    SDL_PIXELFORMAT_YV12 = ... , 
    SDL_PIXELFORMAT_IYUV = ... ,
    SDL_PIXELFORMAT_YUY2 = ... ,
    SDL_PIXELFORMAT_UYVY = ... ,
    SDL_PIXELFORMAT_YVYU = ... 
};
typedef struct SDL_Color
{
    Uint8 r;
    Uint8 g;
    Uint8 b;
    Uint8 a;
} SDL_Color;
typedef struct SDL_Palette
{
    int ncolors;
    SDL_Color *colors;
    Uint32 version;
    int refcount;
} SDL_Palette;
typedef struct SDL_PixelFormat
{
    Uint32 format;
    SDL_Palette *palette;
    Uint8 BitsPerPixel;
    Uint8 BytesPerPixel;
    Uint8 padding[2];
    Uint32 Rmask;
    Uint32 Gmask;
    Uint32 Bmask;
    Uint32 Amask;
    Uint8 Rloss;
    Uint8 Gloss;
    Uint8 Bloss;
    Uint8 Aloss;
    Uint8 Rshift;
    Uint8 Gshift;
    Uint8 Bshift;
    Uint8 Ashift;
    int refcount;
    struct SDL_PixelFormat *next;
} SDL_PixelFormat;
extern const char* SDL_GetPixelFormatName(Uint32 format);
extern SDL_bool SDL_PixelFormatEnumToMasks(Uint32 format,
                                                            int *bpp,
                                                            Uint32 * Rmask,
                                                            Uint32 * Gmask,
                                                            Uint32 * Bmask,
                                                            Uint32 * Amask);
extern Uint32 SDL_MasksToPixelFormatEnum(int bpp,
                                                          Uint32 Rmask,
                                                          Uint32 Gmask,
                                                          Uint32 Bmask,
                                                          Uint32 Amask);
extern SDL_PixelFormat * SDL_AllocFormat(Uint32 pixel_format);
extern void SDL_FreeFormat(SDL_PixelFormat *format);
extern SDL_Palette * SDL_AllocPalette(int ncolors);
extern int SDL_SetPixelFormatPalette(SDL_PixelFormat * format,
                                                      SDL_Palette *palette);
extern int SDL_SetPaletteColors(SDL_Palette * palette,
                                                 const SDL_Color * colors,
                                                 int firstcolor, int ncolors);
extern void SDL_FreePalette(SDL_Palette * palette);
extern Uint32 SDL_MapRGB(const SDL_PixelFormat * format,
                                          Uint8 r, Uint8 g, Uint8 b);
extern Uint32 SDL_MapRGBA(const SDL_PixelFormat * format,
                                           Uint8 r, Uint8 g, Uint8 b,
                                           Uint8 a);
extern void SDL_GetRGB(Uint32 pixel,
                                        const SDL_PixelFormat * format,
                                        Uint8 * r, Uint8 * g, Uint8 * b);
extern void SDL_GetRGBA(Uint32 pixel,
                                         const SDL_PixelFormat * format,
                                         Uint8 * r, Uint8 * g, Uint8 * b,
                                         Uint8 * a);
extern void SDL_CalculateGammaRamp(float gamma, Uint16 * ramp);
typedef struct SDL_Point
{
    int x;
    int y;
} SDL_Point;
typedef struct SDL_Rect
{
    int x, y;
    int w, h;
} SDL_Rect;
extern SDL_bool SDL_HasIntersection(const SDL_Rect * A,
                                                     const SDL_Rect * B);
extern SDL_bool SDL_IntersectRect(const SDL_Rect * A,
                                                   const SDL_Rect * B,
                                                   SDL_Rect * result);
extern void SDL_UnionRect(const SDL_Rect * A,
                                           const SDL_Rect * B,
                                           SDL_Rect * result);
extern SDL_bool SDL_EnclosePoints(const SDL_Point * points,
                                                   int count,
                                                   const SDL_Rect * clip,
                                                   SDL_Rect * result);
extern SDL_bool SDL_IntersectRectAndLine(const SDL_Rect *
                                                          rect, int *X1,
                                                          int *Y1, int *X2,
                                                          int *Y2);
typedef enum
{
    SDL_BLENDMODE_NONE = 0x00000000,
    SDL_BLENDMODE_BLEND = 0x00000001,
    SDL_BLENDMODE_ADD = 0x00000002,
    SDL_BLENDMODE_MOD = 0x00000004
} SDL_BlendMode;
typedef struct SDL_Surface
{
    Uint32 flags;
    SDL_PixelFormat *format;
    int w, h;
    int pitch;
    void *pixels;
    void *userdata;
    int locked;
    void *lock_data;
    SDL_Rect clip_rect;
    struct SDL_BlitMap *map;
    int refcount;
} SDL_Surface;
typedef int (*SDL_blit) (struct SDL_Surface * src, SDL_Rect * srcrect,
                         struct SDL_Surface * dst, SDL_Rect * dstrect);
extern SDL_Surface * SDL_CreateRGBSurface
    (Uint32 flags, int width, int height, int depth,
     Uint32 Rmask, Uint32 Gmask, Uint32 Bmask, Uint32 Amask);
extern SDL_Surface * SDL_CreateRGBSurfaceFrom(void *pixels,
                                                              int width,
                                                              int height,
                                                              int depth,
                                                              int pitch,
                                                              Uint32 Rmask,
                                                              Uint32 Gmask,
                                                              Uint32 Bmask,
                                                              Uint32 Amask);
extern void SDL_FreeSurface(SDL_Surface * surface);
extern int SDL_SetSurfacePalette(SDL_Surface * surface,
                                                  SDL_Palette * palette);
extern int SDL_LockSurface(SDL_Surface * surface);
extern void SDL_UnlockSurface(SDL_Surface * surface);
extern SDL_Surface * SDL_LoadBMP_RW(SDL_RWops * src,
                                                    int freesrc);
extern int SDL_SaveBMP_RW
    (SDL_Surface * surface, SDL_RWops * dst, int freedst);
extern int SDL_SetSurfaceRLE(SDL_Surface * surface,
                                              int flag);
extern int SDL_SetColorKey(SDL_Surface * surface,
                                            int flag, Uint32 key);
extern int SDL_GetColorKey(SDL_Surface * surface,
                                            Uint32 * key);
extern int SDL_SetSurfaceColorMod(SDL_Surface * surface,
                                                   Uint8 r, Uint8 g, Uint8 b);
extern int SDL_GetSurfaceColorMod(SDL_Surface * surface,
                                                   Uint8 * r, Uint8 * g,
                                                   Uint8 * b);
extern int SDL_SetSurfaceAlphaMod(SDL_Surface * surface,
                                                   Uint8 alpha);
extern int SDL_GetSurfaceAlphaMod(SDL_Surface * surface,
                                                   Uint8 * alpha);
extern int SDL_SetSurfaceBlendMode(SDL_Surface * surface,
                                                    SDL_BlendMode blendMode);
extern int SDL_GetSurfaceBlendMode(SDL_Surface * surface,
                                                    SDL_BlendMode *blendMode);
extern SDL_bool SDL_SetClipRect(SDL_Surface * surface,
                                                 const SDL_Rect * rect);
extern void SDL_GetClipRect(SDL_Surface * surface,
                                             SDL_Rect * rect);
extern SDL_Surface * SDL_ConvertSurface
    (SDL_Surface * src, const SDL_PixelFormat * fmt, Uint32 flags);
extern SDL_Surface * SDL_ConvertSurfaceFormat
    (SDL_Surface * src, Uint32 pixel_format, Uint32 flags);
extern int SDL_ConvertPixels(int width, int height,
                                              Uint32 src_format,
                                              const void * src, int src_pitch,
                                              Uint32 dst_format,
                                              void * dst, int dst_pitch);
extern int SDL_FillRect
    (SDL_Surface * dst, const SDL_Rect * rect, Uint32 color);
extern int SDL_FillRects
    (SDL_Surface * dst, const SDL_Rect * rects, int count, Uint32 color);
extern int SDL_UpperBlit
    (SDL_Surface * src, const SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);
extern int SDL_LowerBlit
    (SDL_Surface * src, SDL_Rect * srcrect,
     SDL_Surface * dst, SDL_Rect * dstrect);
extern int SDL_SoftStretch(SDL_Surface * src,
                                            const SDL_Rect * srcrect,
                                            SDL_Surface * dst,
                                            const SDL_Rect * dstrect);
extern int SDL_UpperBlitScaled
    (SDL_Surface * src, const SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);
extern int SDL_LowerBlitScaled
    (SDL_Surface * src, SDL_Rect * srcrect,
    SDL_Surface * dst, SDL_Rect * dstrect);
typedef struct
{
    Uint32 format;
    int w;
    int h;
    int refresh_rate;
    void *driverdata;
} SDL_DisplayMode;
typedef struct SDL_Window SDL_Window;
typedef enum
{
    SDL_WINDOW_FULLSCREEN = 0x00000001,
    SDL_WINDOW_OPENGL = 0x00000002,
    SDL_WINDOW_SHOWN = 0x00000004,
    SDL_WINDOW_HIDDEN = 0x00000008,
    SDL_WINDOW_BORDERLESS = 0x00000010,
    SDL_WINDOW_RESIZABLE = 0x00000020,
    SDL_WINDOW_MINIMIZED = 0x00000040,
    SDL_WINDOW_MAXIMIZED = 0x00000080,
    SDL_WINDOW_INPUT_GRABBED = 0x00000100,
    SDL_WINDOW_INPUT_FOCUS = 0x00000200,
    SDL_WINDOW_MOUSE_FOCUS = 0x00000400,
    SDL_WINDOW_FULLSCREEN_DESKTOP = ... ,
    SDL_WINDOW_FOREIGN = 0x00000800,
    SDL_WINDOW_ALLOW_HIGHDPI = 0x00002000
} SDL_WindowFlags;
typedef enum
{
    SDL_WINDOWEVENT_NONE,
    SDL_WINDOWEVENT_SHOWN,
    SDL_WINDOWEVENT_HIDDEN,
    SDL_WINDOWEVENT_EXPOSED,
    SDL_WINDOWEVENT_MOVED,
    SDL_WINDOWEVENT_RESIZED,
    SDL_WINDOWEVENT_SIZE_CHANGED,
    SDL_WINDOWEVENT_MINIMIZED,
    SDL_WINDOWEVENT_MAXIMIZED,
    SDL_WINDOWEVENT_RESTORED,
    SDL_WINDOWEVENT_ENTER,
    SDL_WINDOWEVENT_LEAVE,
    SDL_WINDOWEVENT_FOCUS_GAINED,
    SDL_WINDOWEVENT_FOCUS_LOST,
    SDL_WINDOWEVENT_CLOSE
} SDL_WindowEventID;
typedef void *SDL_GLContext;
typedef enum
{
    SDL_GL_RED_SIZE,
    SDL_GL_GREEN_SIZE,
    SDL_GL_BLUE_SIZE,
    SDL_GL_ALPHA_SIZE,
    SDL_GL_BUFFER_SIZE,
    SDL_GL_DOUBLEBUFFER,
    SDL_GL_DEPTH_SIZE,
    SDL_GL_STENCIL_SIZE,
    SDL_GL_ACCUM_RED_SIZE,
    SDL_GL_ACCUM_GREEN_SIZE,
    SDL_GL_ACCUM_BLUE_SIZE,
    SDL_GL_ACCUM_ALPHA_SIZE,
    SDL_GL_STEREO,
    SDL_GL_MULTISAMPLEBUFFERS,
    SDL_GL_MULTISAMPLESAMPLES,
    SDL_GL_ACCELERATED_VISUAL,
    SDL_GL_RETAINED_BACKING,
    SDL_GL_CONTEXT_MAJOR_VERSION,
    SDL_GL_CONTEXT_MINOR_VERSION,
    SDL_GL_CONTEXT_EGL,
    SDL_GL_CONTEXT_FLAGS,
    SDL_GL_CONTEXT_PROFILE_MASK,
    SDL_GL_SHARE_WITH_CURRENT_CONTEXT,
    SDL_GL_FRAMEBUFFER_SRGB_CAPABLE
} SDL_GLattr;
typedef enum
{
    SDL_GL_CONTEXT_PROFILE_CORE = 0x0001,
    SDL_GL_CONTEXT_PROFILE_COMPATIBILITY = 0x0002,
    SDL_GL_CONTEXT_PROFILE_ES = 0x0004
} SDL_GLprofile;
typedef enum
{
    SDL_GL_CONTEXT_DEBUG_FLAG = 0x0001,
    SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG = 0x0002,
    SDL_GL_CONTEXT_ROBUST_ACCESS_FLAG = 0x0004,
    SDL_GL_CONTEXT_RESET_ISOLATION_FLAG = 0x0008
} SDL_GLcontextFlag;
extern int SDL_GetNumVideoDrivers(void);
extern const char * SDL_GetVideoDriver(int index);
extern int SDL_VideoInit(const char *driver_name);
extern void SDL_VideoQuit(void);
extern const char * SDL_GetCurrentVideoDriver(void);
extern int SDL_GetNumVideoDisplays(void);
extern const char * SDL_GetDisplayName(int displayIndex);
extern int SDL_GetDisplayBounds(int displayIndex, SDL_Rect * rect);
extern int SDL_GetNumDisplayModes(int displayIndex);
extern int SDL_GetDisplayMode(int displayIndex, int modeIndex,
                                               SDL_DisplayMode * mode);
extern int SDL_GetDesktopDisplayMode(int displayIndex, SDL_DisplayMode * mode);
extern int SDL_GetCurrentDisplayMode(int displayIndex, SDL_DisplayMode * mode);
extern SDL_DisplayMode * SDL_GetClosestDisplayMode(int displayIndex, const SDL_DisplayMode * mode, SDL_DisplayMode * closest);
extern int SDL_GetWindowDisplayIndex(SDL_Window * window);
extern int SDL_SetWindowDisplayMode(SDL_Window * window,
                                                     const SDL_DisplayMode
                                                         * mode);
extern int SDL_GetWindowDisplayMode(SDL_Window * window,
                                                     SDL_DisplayMode * mode);
extern Uint32 SDL_GetWindowPixelFormat(SDL_Window * window);
extern SDL_Window * SDL_CreateWindow(const char *title,
                                                      int x, int y, int w,
                                                      int h, Uint32 flags);
extern SDL_Window * SDL_CreateWindowFrom(const void *data);
extern Uint32 SDL_GetWindowID(SDL_Window * window);
extern SDL_Window * SDL_GetWindowFromID(Uint32 id);
extern Uint32 SDL_GetWindowFlags(SDL_Window * window);
extern void SDL_SetWindowTitle(SDL_Window * window,
                                                const char *title);
extern const char * SDL_GetWindowTitle(SDL_Window * window);
extern void SDL_SetWindowIcon(SDL_Window * window,
                                               SDL_Surface * icon);
extern void* SDL_SetWindowData(SDL_Window * window,
                                                const char *name,
                                                void *userdata);
extern void * SDL_GetWindowData(SDL_Window * window,
                                                const char *name);
extern void SDL_SetWindowPosition(SDL_Window * window,
                                                   int x, int y);
extern void SDL_GetWindowPosition(SDL_Window * window,
                                                   int *x, int *y);
extern void SDL_SetWindowSize(SDL_Window * window, int w,
                                               int h);
extern void SDL_GetWindowSize(SDL_Window * window, int *w,
                                               int *h);
extern void SDL_SetWindowMinimumSize(SDL_Window * window,
                                                      int min_w, int min_h);
extern void SDL_GetWindowMinimumSize(SDL_Window * window,
                                                      int *w, int *h);
extern void SDL_SetWindowMaximumSize(SDL_Window * window,
                                                      int max_w, int max_h);
extern void SDL_GetWindowMaximumSize(SDL_Window * window,
                                                      int *w, int *h);
extern void SDL_SetWindowBordered(SDL_Window * window,
                                                   SDL_bool bordered);
extern void SDL_ShowWindow(SDL_Window * window);
extern void SDL_HideWindow(SDL_Window * window);
extern void SDL_RaiseWindow(SDL_Window * window);
extern void SDL_MaximizeWindow(SDL_Window * window);
extern void SDL_MinimizeWindow(SDL_Window * window);
extern void SDL_RestoreWindow(SDL_Window * window);
extern int SDL_SetWindowFullscreen(SDL_Window * window,
                                                    Uint32 flags);
extern SDL_Surface * SDL_GetWindowSurface(SDL_Window * window);
extern int SDL_UpdateWindowSurface(SDL_Window * window);
extern int SDL_UpdateWindowSurfaceRects(SDL_Window * window,
                                                         const SDL_Rect * rects,
                                                         int numrects);
extern void SDL_SetWindowGrab(SDL_Window * window,
                                               SDL_bool grabbed);
extern SDL_bool SDL_GetWindowGrab(SDL_Window * window);
extern int SDL_SetWindowBrightness(SDL_Window * window, float brightness);
extern float SDL_GetWindowBrightness(SDL_Window * window);
extern int SDL_SetWindowGammaRamp(SDL_Window * window,
                                                   const Uint16 * red,
                                                   const Uint16 * green,
                                                   const Uint16 * blue);
extern int SDL_GetWindowGammaRamp(SDL_Window * window,
                                                   Uint16 * red,
                                                   Uint16 * green,
                                                   Uint16 * blue);
extern void SDL_DestroyWindow(SDL_Window * window);
extern SDL_bool SDL_IsScreenSaverEnabled(void);
extern void SDL_EnableScreenSaver(void);
extern void SDL_DisableScreenSaver(void);
extern int SDL_GL_LoadLibrary(const char *path);
extern void * SDL_GL_GetProcAddress(const char *proc);
extern void SDL_GL_UnloadLibrary(void);
extern SDL_bool SDL_GL_ExtensionSupported(const char
                                                           *extension);
extern void SDL_GL_ResetAttributes(void);
extern int SDL_GL_SetAttribute(SDL_GLattr attr, int value);
extern int SDL_GL_GetAttribute(SDL_GLattr attr, int *value);
extern SDL_GLContext SDL_GL_CreateContext(SDL_Window *
                                                           window);
extern int SDL_GL_MakeCurrent(SDL_Window * window,
                                               SDL_GLContext context);
extern SDL_Window* SDL_GL_GetCurrentWindow(void);
extern SDL_GLContext SDL_GL_GetCurrentContext(void);
extern void SDL_GL_GetDrawableSize(SDL_Window * window, int *w,
                                                    int *h);
extern int SDL_GL_SetSwapInterval(int interval);
extern int SDL_GL_GetSwapInterval(void);
extern void SDL_GL_SwapWindow(SDL_Window * window);
extern void SDL_GL_DeleteContext(SDL_GLContext context);
typedef enum
{
    SDL_SCANCODE_UNKNOWN = 0,
    SDL_SCANCODE_A = 4,
    SDL_SCANCODE_B = 5,
    SDL_SCANCODE_C = 6,
    SDL_SCANCODE_D = 7,
    SDL_SCANCODE_E = 8,
    SDL_SCANCODE_F = 9,
    SDL_SCANCODE_G = 10,
    SDL_SCANCODE_H = 11,
    SDL_SCANCODE_I = 12,
    SDL_SCANCODE_J = 13,
    SDL_SCANCODE_K = 14,
    SDL_SCANCODE_L = 15,
    SDL_SCANCODE_M = 16,
    SDL_SCANCODE_N = 17,
    SDL_SCANCODE_O = 18,
    SDL_SCANCODE_P = 19,
    SDL_SCANCODE_Q = 20,
    SDL_SCANCODE_R = 21,
    SDL_SCANCODE_S = 22,
    SDL_SCANCODE_T = 23,
    SDL_SCANCODE_U = 24,
    SDL_SCANCODE_V = 25,
    SDL_SCANCODE_W = 26,
    SDL_SCANCODE_X = 27,
    SDL_SCANCODE_Y = 28,
    SDL_SCANCODE_Z = 29,
    SDL_SCANCODE_1 = 30,
    SDL_SCANCODE_2 = 31,
    SDL_SCANCODE_3 = 32,
    SDL_SCANCODE_4 = 33,
    SDL_SCANCODE_5 = 34,
    SDL_SCANCODE_6 = 35,
    SDL_SCANCODE_7 = 36,
    SDL_SCANCODE_8 = 37,
    SDL_SCANCODE_9 = 38,
    SDL_SCANCODE_0 = 39,
    SDL_SCANCODE_RETURN = 40,
    SDL_SCANCODE_ESCAPE = 41,
    SDL_SCANCODE_BACKSPACE = 42,
    SDL_SCANCODE_TAB = 43,
    SDL_SCANCODE_SPACE = 44,
    SDL_SCANCODE_MINUS = 45,
    SDL_SCANCODE_EQUALS = 46,
    SDL_SCANCODE_LEFTBRACKET = 47,
    SDL_SCANCODE_RIGHTBRACKET = 48,
    SDL_SCANCODE_BACKSLASH = 49,
    SDL_SCANCODE_NONUSHASH = 50,
    SDL_SCANCODE_SEMICOLON = 51,
    SDL_SCANCODE_APOSTROPHE = 52,
    SDL_SCANCODE_GRAVE = 53,
    SDL_SCANCODE_COMMA = 54,
    SDL_SCANCODE_PERIOD = 55,
    SDL_SCANCODE_SLASH = 56,
    SDL_SCANCODE_CAPSLOCK = 57,
    SDL_SCANCODE_F1 = 58,
    SDL_SCANCODE_F2 = 59,
    SDL_SCANCODE_F3 = 60,
    SDL_SCANCODE_F4 = 61,
    SDL_SCANCODE_F5 = 62,
    SDL_SCANCODE_F6 = 63,
    SDL_SCANCODE_F7 = 64,
    SDL_SCANCODE_F8 = 65,
    SDL_SCANCODE_F9 = 66,
    SDL_SCANCODE_F10 = 67,
    SDL_SCANCODE_F11 = 68,
    SDL_SCANCODE_F12 = 69,
    SDL_SCANCODE_PRINTSCREEN = 70,
    SDL_SCANCODE_SCROLLLOCK = 71,
    SDL_SCANCODE_PAUSE = 72,
    SDL_SCANCODE_INSERT = 73,
    SDL_SCANCODE_HOME = 74,
    SDL_SCANCODE_PAGEUP = 75,
    SDL_SCANCODE_DELETE = 76,
    SDL_SCANCODE_END = 77,
    SDL_SCANCODE_PAGEDOWN = 78,
    SDL_SCANCODE_RIGHT = 79,
    SDL_SCANCODE_LEFT = 80,
    SDL_SCANCODE_DOWN = 81,
    SDL_SCANCODE_UP = 82,
    SDL_SCANCODE_NUMLOCKCLEAR = 83,
    SDL_SCANCODE_KP_DIVIDE = 84,
    SDL_SCANCODE_KP_MULTIPLY = 85,
    SDL_SCANCODE_KP_MINUS = 86,
    SDL_SCANCODE_KP_PLUS = 87,
    SDL_SCANCODE_KP_ENTER = 88,
    SDL_SCANCODE_KP_1 = 89,
    SDL_SCANCODE_KP_2 = 90,
    SDL_SCANCODE_KP_3 = 91,
    SDL_SCANCODE_KP_4 = 92,
    SDL_SCANCODE_KP_5 = 93,
    SDL_SCANCODE_KP_6 = 94,
    SDL_SCANCODE_KP_7 = 95,
    SDL_SCANCODE_KP_8 = 96,
    SDL_SCANCODE_KP_9 = 97,
    SDL_SCANCODE_KP_0 = 98,
    SDL_SCANCODE_KP_PERIOD = 99,
    SDL_SCANCODE_NONUSBACKSLASH = 100,
    SDL_SCANCODE_APPLICATION = 101,
    SDL_SCANCODE_POWER = 102,
    SDL_SCANCODE_KP_EQUALS = 103,
    SDL_SCANCODE_F13 = 104,
    SDL_SCANCODE_F14 = 105,
    SDL_SCANCODE_F15 = 106,
    SDL_SCANCODE_F16 = 107,
    SDL_SCANCODE_F17 = 108,
    SDL_SCANCODE_F18 = 109,
    SDL_SCANCODE_F19 = 110,
    SDL_SCANCODE_F20 = 111,
    SDL_SCANCODE_F21 = 112,
    SDL_SCANCODE_F22 = 113,
    SDL_SCANCODE_F23 = 114,
    SDL_SCANCODE_F24 = 115,
    SDL_SCANCODE_EXECUTE = 116,
    SDL_SCANCODE_HELP = 117,
    SDL_SCANCODE_MENU = 118,
    SDL_SCANCODE_SELECT = 119,
    SDL_SCANCODE_STOP = 120,
    SDL_SCANCODE_AGAIN = 121,
    SDL_SCANCODE_UNDO = 122,
    SDL_SCANCODE_CUT = 123,
    SDL_SCANCODE_COPY = 124,
    SDL_SCANCODE_PASTE = 125,
    SDL_SCANCODE_FIND = 126,
    SDL_SCANCODE_MUTE = 127,
    SDL_SCANCODE_VOLUMEUP = 128,
    SDL_SCANCODE_VOLUMEDOWN = 129,
    SDL_SCANCODE_KP_COMMA = 133,
    SDL_SCANCODE_KP_EQUALSAS400 = 134,
    SDL_SCANCODE_INTERNATIONAL1 = 135,
    SDL_SCANCODE_INTERNATIONAL2 = 136,
    SDL_SCANCODE_INTERNATIONAL3 = 137,
    SDL_SCANCODE_INTERNATIONAL4 = 138,
    SDL_SCANCODE_INTERNATIONAL5 = 139,
    SDL_SCANCODE_INTERNATIONAL6 = 140,
    SDL_SCANCODE_INTERNATIONAL7 = 141,
    SDL_SCANCODE_INTERNATIONAL8 = 142,
    SDL_SCANCODE_INTERNATIONAL9 = 143,
    SDL_SCANCODE_LANG1 = 144,
    SDL_SCANCODE_LANG2 = 145,
    SDL_SCANCODE_LANG3 = 146,
    SDL_SCANCODE_LANG4 = 147,
    SDL_SCANCODE_LANG5 = 148,
    SDL_SCANCODE_LANG6 = 149,
    SDL_SCANCODE_LANG7 = 150,
    SDL_SCANCODE_LANG8 = 151,
    SDL_SCANCODE_LANG9 = 152,
    SDL_SCANCODE_ALTERASE = 153,
    SDL_SCANCODE_SYSREQ = 154,
    SDL_SCANCODE_CANCEL = 155,
    SDL_SCANCODE_CLEAR = 156,
    SDL_SCANCODE_PRIOR = 157,
    SDL_SCANCODE_RETURN2 = 158,
    SDL_SCANCODE_SEPARATOR = 159,
    SDL_SCANCODE_OUT = 160,
    SDL_SCANCODE_OPER = 161,
    SDL_SCANCODE_CLEARAGAIN = 162,
    SDL_SCANCODE_CRSEL = 163,
    SDL_SCANCODE_EXSEL = 164,
    SDL_SCANCODE_KP_00 = 176,
    SDL_SCANCODE_KP_000 = 177,
    SDL_SCANCODE_THOUSANDSSEPARATOR = 178,
    SDL_SCANCODE_DECIMALSEPARATOR = 179,
    SDL_SCANCODE_CURRENCYUNIT = 180,
    SDL_SCANCODE_CURRENCYSUBUNIT = 181,
    SDL_SCANCODE_KP_LEFTPAREN = 182,
    SDL_SCANCODE_KP_RIGHTPAREN = 183,
    SDL_SCANCODE_KP_LEFTBRACE = 184,
    SDL_SCANCODE_KP_RIGHTBRACE = 185,
    SDL_SCANCODE_KP_TAB = 186,
    SDL_SCANCODE_KP_BACKSPACE = 187,
    SDL_SCANCODE_KP_A = 188,
    SDL_SCANCODE_KP_B = 189,
    SDL_SCANCODE_KP_C = 190,
    SDL_SCANCODE_KP_D = 191,
    SDL_SCANCODE_KP_E = 192,
    SDL_SCANCODE_KP_F = 193,
    SDL_SCANCODE_KP_XOR = 194,
    SDL_SCANCODE_KP_POWER = 195,
    SDL_SCANCODE_KP_PERCENT = 196,
    SDL_SCANCODE_KP_LESS = 197,
    SDL_SCANCODE_KP_GREATER = 198,
    SDL_SCANCODE_KP_AMPERSAND = 199,
    SDL_SCANCODE_KP_DBLAMPERSAND = 200,
    SDL_SCANCODE_KP_VERTICALBAR = 201,
    SDL_SCANCODE_KP_DBLVERTICALBAR = 202,
    SDL_SCANCODE_KP_COLON = 203,
    SDL_SCANCODE_KP_HASH = 204,
    SDL_SCANCODE_KP_SPACE = 205,
    SDL_SCANCODE_KP_AT = 206,
    SDL_SCANCODE_KP_EXCLAM = 207,
    SDL_SCANCODE_KP_MEMSTORE = 208,
    SDL_SCANCODE_KP_MEMRECALL = 209,
    SDL_SCANCODE_KP_MEMCLEAR = 210,
    SDL_SCANCODE_KP_MEMADD = 211,
    SDL_SCANCODE_KP_MEMSUBTRACT = 212,
    SDL_SCANCODE_KP_MEMMULTIPLY = 213,
    SDL_SCANCODE_KP_MEMDIVIDE = 214,
    SDL_SCANCODE_KP_PLUSMINUS = 215,
    SDL_SCANCODE_KP_CLEAR = 216,
    SDL_SCANCODE_KP_CLEARENTRY = 217,
    SDL_SCANCODE_KP_BINARY = 218,
    SDL_SCANCODE_KP_OCTAL = 219,
    SDL_SCANCODE_KP_DECIMAL = 220,
    SDL_SCANCODE_KP_HEXADECIMAL = 221,
    SDL_SCANCODE_LCTRL = 224,
    SDL_SCANCODE_LSHIFT = 225,
    SDL_SCANCODE_LALT = 226,
    SDL_SCANCODE_LGUI = 227,
    SDL_SCANCODE_RCTRL = 228,
    SDL_SCANCODE_RSHIFT = 229,
    SDL_SCANCODE_RALT = 230,
    SDL_SCANCODE_RGUI = 231,
    SDL_SCANCODE_MODE = 257,
    SDL_SCANCODE_AUDIONEXT = 258,
    SDL_SCANCODE_AUDIOPREV = 259,
    SDL_SCANCODE_AUDIOSTOP = 260,
    SDL_SCANCODE_AUDIOPLAY = 261,
    SDL_SCANCODE_AUDIOMUTE = 262,
    SDL_SCANCODE_MEDIASELECT = 263,
    SDL_SCANCODE_WWW = 264,
    SDL_SCANCODE_MAIL = 265,
    SDL_SCANCODE_CALCULATOR = 266,
    SDL_SCANCODE_COMPUTER = 267,
    SDL_SCANCODE_AC_SEARCH = 268,
    SDL_SCANCODE_AC_HOME = 269,
    SDL_SCANCODE_AC_BACK = 270,
    SDL_SCANCODE_AC_FORWARD = 271,
    SDL_SCANCODE_AC_STOP = 272,
    SDL_SCANCODE_AC_REFRESH = 273,
    SDL_SCANCODE_AC_BOOKMARKS = 274,
    SDL_SCANCODE_BRIGHTNESSDOWN = 275,
    SDL_SCANCODE_BRIGHTNESSUP = 276,
    SDL_SCANCODE_DISPLAYSWITCH = 277,
    SDL_SCANCODE_KBDILLUMTOGGLE = 278,
    SDL_SCANCODE_KBDILLUMDOWN = 279,
    SDL_SCANCODE_KBDILLUMUP = 280,
    SDL_SCANCODE_EJECT = 281,
    SDL_SCANCODE_SLEEP = 282,
    SDL_SCANCODE_APP1 = 283,
    SDL_SCANCODE_APP2 = 284,
    SDL_NUM_SCANCODES = 512
} SDL_Scancode;
typedef Sint32 SDL_Keycode;
enum
{
    SDLK_UNKNOWN = ...,
    SDLK_RETURN = ...,
    SDLK_ESCAPE = ...,
    SDLK_BACKSPACE = ...,
    SDLK_TAB = ...,
    SDLK_SPACE = ...,
    SDLK_EXCLAIM = ...,
    SDLK_QUOTEDBL = ...,
    SDLK_HASH = ...,
    SDLK_PERCENT = ...,
    SDLK_DOLLAR = ...,
    SDLK_AMPERSAND = ...,
    SDLK_QUOTE = ...,
    SDLK_LEFTPAREN = ...,
    SDLK_RIGHTPAREN = ...,
    SDLK_ASTERISK = ...,
    SDLK_PLUS = ...,
    SDLK_COMMA = ...,
    SDLK_MINUS = ...,
    SDLK_PERIOD = ...,
    SDLK_SLASH = ...,
    SDLK_0 = ...,
    SDLK_1 = ...,
    SDLK_2 = ...,
    SDLK_3 = ...,
    SDLK_4 = ...,
    SDLK_5 = ...,
    SDLK_6 = ...,
    SDLK_7 = ...,
    SDLK_8 = ...,
    SDLK_9 = ...,
    SDLK_COLON = ...,
    SDLK_SEMICOLON = ...,
    SDLK_LESS = ...,
    SDLK_EQUALS = ...,
    SDLK_GREATER = ...,
    SDLK_QUESTION = ...,
    SDLK_AT = ...,
    SDLK_LEFTBRACKET = ...,
    SDLK_BACKSLASH = ...,
    SDLK_RIGHTBRACKET = ...,
    SDLK_CARET = ...,
    SDLK_UNDERSCORE = ...,
    SDLK_BACKQUOTE = ...,
    SDLK_a = ...,
    SDLK_b = ...,
    SDLK_c = ...,
    SDLK_d = ...,
    SDLK_e = ...,
    SDLK_f = ...,
    SDLK_g = ...,
    SDLK_h = ...,
    SDLK_i = ...,
    SDLK_j = ...,
    SDLK_k = ...,
    SDLK_l = ...,
    SDLK_m = ...,
    SDLK_n = ...,
    SDLK_o = ...,
    SDLK_p = ...,
    SDLK_q = ...,
    SDLK_r = ...,
    SDLK_s = ...,
    SDLK_t = ...,
    SDLK_u = ...,
    SDLK_v = ...,
    SDLK_w = ...,
    SDLK_x = ...,
    SDLK_y = ...,
    SDLK_z = ...,
    SDLK_CAPSLOCK = ...,
    SDLK_F1 = ...,
    SDLK_F2 = ...,
    SDLK_F3 = ...,
    SDLK_F4 = ...,
    SDLK_F5 = ...,
    SDLK_F6 = ...,
    SDLK_F7 = ...,
    SDLK_F8 = ...,
    SDLK_F9 = ...,
    SDLK_F10 = ...,
    SDLK_F11 = ...,
    SDLK_F12 = ...,
    SDLK_PRINTSCREEN = ...,
    SDLK_SCROLLLOCK = ...,
    SDLK_PAUSE = ...,
    SDLK_INSERT = ...,
    SDLK_HOME = ...,
    SDLK_PAGEUP = ...,
    SDLK_DELETE = ...,
    SDLK_END = ...,
    SDLK_PAGEDOWN = ...,
    SDLK_RIGHT = ...,
    SDLK_LEFT = ...,
    SDLK_DOWN = ...,
    SDLK_UP = ...,
    SDLK_NUMLOCKCLEAR = ...,
    SDLK_KP_DIVIDE = ...,
    SDLK_KP_MULTIPLY = ...,
    SDLK_KP_MINUS = ...,
    SDLK_KP_PLUS = ...,
    SDLK_KP_ENTER = ...,
    SDLK_KP_1 = ...,
    SDLK_KP_2 = ...,
    SDLK_KP_3 = ...,
    SDLK_KP_4 = ...,
    SDLK_KP_5 = ...,
    SDLK_KP_6 = ...,
    SDLK_KP_7 = ...,
    SDLK_KP_8 = ...,
    SDLK_KP_9 = ...,
    SDLK_KP_0 = ...,
    SDLK_KP_PERIOD = ...,
    SDLK_APPLICATION = ...,
    SDLK_POWER = ...,
    SDLK_KP_EQUALS = ...,
    SDLK_F13 = ...,
    SDLK_F14 = ...,
    SDLK_F15 = ...,
    SDLK_F16 = ...,
    SDLK_F17 = ...,
    SDLK_F18 = ...,
    SDLK_F19 = ...,
    SDLK_F20 = ...,
    SDLK_F21 = ...,
    SDLK_F22 = ...,
    SDLK_F23 = ...,
    SDLK_F24 = ...,
    SDLK_EXECUTE = ...,
    SDLK_HELP = ...,
    SDLK_MENU = ...,
    SDLK_SELECT = ...,
    SDLK_STOP = ...,
    SDLK_AGAIN = ...,
    SDLK_UNDO = ...,
    SDLK_CUT = ...,
    SDLK_COPY = ...,
    SDLK_PASTE = ...,
    SDLK_FIND = ...,
    SDLK_MUTE = ...,
    SDLK_VOLUMEUP = ...,
    SDLK_VOLUMEDOWN = ...,
    SDLK_KP_COMMA = ...,
    SDLK_KP_EQUALSAS400 = ...,
    SDLK_ALTERASE = ...,
    SDLK_SYSREQ = ...,
    SDLK_CANCEL = ...,
    SDLK_CLEAR = ...,
    SDLK_PRIOR = ...,
    SDLK_RETURN2 = ...,
    SDLK_SEPARATOR = ...,
    SDLK_OUT = ...,
    SDLK_OPER = ...,
    SDLK_CLEARAGAIN = ...,
    SDLK_CRSEL = ...,
    SDLK_EXSEL = ...,
    SDLK_KP_00 = ...,
    SDLK_KP_000 = ...,
    SDLK_THOUSANDSSEPARATOR = ...,
    SDLK_DECIMALSEPARATOR = ...,
    SDLK_CURRENCYUNIT = ...,
    SDLK_CURRENCYSUBUNIT = ...,
    SDLK_KP_LEFTPAREN = ...,
    SDLK_KP_RIGHTPAREN = ...,
    SDLK_KP_LEFTBRACE = ...,
    SDLK_KP_RIGHTBRACE = ...,
    SDLK_KP_TAB = ...,
    SDLK_KP_BACKSPACE = ...,
    SDLK_KP_A = ...,
    SDLK_KP_B = ...,
    SDLK_KP_C = ...,
    SDLK_KP_D = ...,
    SDLK_KP_E = ...,
    SDLK_KP_F = ...,
    SDLK_KP_XOR = ...,
    SDLK_KP_POWER = ...,
    SDLK_KP_PERCENT = ...,
    SDLK_KP_LESS = ...,
    SDLK_KP_GREATER = ...,
    SDLK_KP_AMPERSAND = ...,
    SDLK_KP_DBLAMPERSAND = ...,
    SDLK_KP_VERTICALBAR = ...,
    SDLK_KP_DBLVERTICALBAR = ...,
    SDLK_KP_COLON = ...,
    SDLK_KP_HASH = ...,
    SDLK_KP_SPACE = ...,
    SDLK_KP_AT = ...,
    SDLK_KP_EXCLAM = ...,
    SDLK_KP_MEMSTORE = ...,
    SDLK_KP_MEMRECALL = ...,
    SDLK_KP_MEMCLEAR = ...,
    SDLK_KP_MEMADD = ...,
    SDLK_KP_MEMSUBTRACT = ...,
    SDLK_KP_MEMMULTIPLY = ...,
    SDLK_KP_MEMDIVIDE = ...,
    SDLK_KP_PLUSMINUS = ...,
    SDLK_KP_CLEAR = ...,
    SDLK_KP_CLEARENTRY = ...,
    SDLK_KP_BINARY = ...,
    SDLK_KP_OCTAL = ...,
    SDLK_KP_DECIMAL = ...,
    SDLK_KP_HEXADECIMAL = ...,
    SDLK_LCTRL = ...,
    SDLK_LSHIFT = ...,
    SDLK_LALT = ...,
    SDLK_LGUI = ...,
    SDLK_RCTRL = ...,
    SDLK_RSHIFT = ...,
    SDLK_RALT = ...,
    SDLK_RGUI = ...,
    SDLK_MODE = ...,
    SDLK_AUDIONEXT = ...,
    SDLK_AUDIOPREV = ...,
    SDLK_AUDIOSTOP = ...,
    SDLK_AUDIOPLAY = ...,
    SDLK_AUDIOMUTE = ...,
    SDLK_MEDIASELECT = ...,
    SDLK_WWW = ...,
    SDLK_MAIL = ...,
    SDLK_CALCULATOR = ...,
    SDLK_COMPUTER = ...,
    SDLK_AC_SEARCH = ...,
    SDLK_AC_HOME = ...,
    SDLK_AC_BACK = ...,
    SDLK_AC_FORWARD = ...,
    SDLK_AC_STOP = ...,
    SDLK_AC_REFRESH = ...,
    SDLK_AC_BOOKMARKS = ...,
    SDLK_BRIGHTNESSDOWN = ...,
    SDLK_BRIGHTNESSUP = ...,
    SDLK_DISPLAYSWITCH = ...,
    SDLK_KBDILLUMTOGGLE = ...,
    SDLK_KBDILLUMDOWN = ...,
    SDLK_KBDILLUMUP = ...,
    SDLK_EJECT = ...,
    SDLK_SLEEP = ...,
};
typedef enum
{
    KMOD_NONE = 0x0000,
    KMOD_LSHIFT = 0x0001,
    KMOD_RSHIFT = 0x0002,
    KMOD_LCTRL = 0x0040,
    KMOD_RCTRL = 0x0080,
    KMOD_LALT = 0x0100,
    KMOD_RALT = 0x0200,
    KMOD_LGUI = 0x0400,
    KMOD_RGUI = 0x0800,
    KMOD_NUM = 0x1000,
    KMOD_CAPS = 0x2000,
    KMOD_MODE = 0x4000,
    KMOD_RESERVED = 0x8000
} SDL_Keymod;
typedef struct SDL_Keysym
{
    SDL_Scancode scancode;
    SDL_Keycode sym;
    Uint16 mod;
    Uint32 unused;
} SDL_Keysym;
extern SDL_Window * SDL_GetKeyboardFocus(void);
extern const Uint8 * SDL_GetKeyboardState(int *numkeys);
extern SDL_Keymod SDL_GetModState(void);
extern void SDL_SetModState(SDL_Keymod modstate);
extern SDL_Keycode SDL_GetKeyFromScancode(SDL_Scancode scancode);
extern SDL_Scancode SDL_GetScancodeFromKey(SDL_Keycode key);
extern const char * SDL_GetScancodeName(SDL_Scancode scancode);
extern SDL_Scancode SDL_GetScancodeFromName(const char *name);
extern const char * SDL_GetKeyName(SDL_Keycode key);
extern SDL_Keycode SDL_GetKeyFromName(const char *name);
extern void SDL_StartTextInput(void);
extern SDL_bool SDL_IsTextInputActive(void);
extern void SDL_StopTextInput(void);
extern void SDL_SetTextInputRect(SDL_Rect *rect);
extern SDL_bool SDL_HasScreenKeyboardSupport(void);
extern SDL_bool SDL_IsScreenKeyboardShown(SDL_Window *window);
typedef struct SDL_Cursor SDL_Cursor;
typedef enum
{
    SDL_SYSTEM_CURSOR_ARROW,
    SDL_SYSTEM_CURSOR_IBEAM,
    SDL_SYSTEM_CURSOR_WAIT,
    SDL_SYSTEM_CURSOR_CROSSHAIR,
    SDL_SYSTEM_CURSOR_WAITARROW,
    SDL_SYSTEM_CURSOR_SIZENWSE,
    SDL_SYSTEM_CURSOR_SIZENESW,
    SDL_SYSTEM_CURSOR_SIZEWE,
    SDL_SYSTEM_CURSOR_SIZENS,
    SDL_SYSTEM_CURSOR_SIZEALL,
    SDL_SYSTEM_CURSOR_NO,
    SDL_SYSTEM_CURSOR_HAND,
    SDL_NUM_SYSTEM_CURSORS
} SDL_SystemCursor;
extern SDL_Window * SDL_GetMouseFocus(void);
extern Uint32 SDL_GetMouseState(int *x, int *y);
extern Uint32 SDL_GetRelativeMouseState(int *x, int *y);
extern void SDL_WarpMouseInWindow(SDL_Window * window,
                                                   int x, int y);
extern int SDL_SetRelativeMouseMode(SDL_bool enabled);
extern SDL_bool SDL_GetRelativeMouseMode(void);
extern SDL_Cursor * SDL_CreateCursor(const Uint8 * data,
                                                     const Uint8 * mask,
                                                     int w, int h, int hot_x,
                                                     int hot_y);
extern SDL_Cursor * SDL_CreateColorCursor(SDL_Surface *surface,
                                                          int hot_x,
                                                          int hot_y);
extern SDL_Cursor * SDL_CreateSystemCursor(SDL_SystemCursor id);
extern void SDL_SetCursor(SDL_Cursor * cursor);
extern SDL_Cursor * SDL_GetCursor(void);
extern SDL_Cursor * SDL_GetDefaultCursor(void);
extern void SDL_FreeCursor(SDL_Cursor * cursor);
extern int SDL_ShowCursor(int toggle);
struct _SDL_Joystick;
typedef struct _SDL_Joystick SDL_Joystick;
typedef struct {
    Uint8 data[16];
} SDL_JoystickGUID;
typedef Sint32 SDL_JoystickID;
extern int SDL_NumJoysticks(void);
extern const char * SDL_JoystickNameForIndex(int device_index);
extern SDL_Joystick * SDL_JoystickOpen(int device_index);
extern const char * SDL_JoystickName(SDL_Joystick * joystick);
extern SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int device_index);
extern SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick * joystick);
extern void SDL_JoystickGetGUIDString(SDL_JoystickGUID guid, char *pszGUID, int cbGUID);
extern SDL_JoystickGUID SDL_JoystickGetGUIDFromString(const char *pchGUID);
extern SDL_bool SDL_JoystickGetAttached(SDL_Joystick * joystick);
extern SDL_JoystickID SDL_JoystickInstanceID(SDL_Joystick * joystick);
extern int SDL_JoystickNumAxes(SDL_Joystick * joystick);
extern int SDL_JoystickNumBalls(SDL_Joystick * joystick);
extern int SDL_JoystickNumHats(SDL_Joystick * joystick);
extern int SDL_JoystickNumButtons(SDL_Joystick * joystick);
extern void SDL_JoystickUpdate(void);
extern int SDL_JoystickEventState(int state);
extern Sint16 SDL_JoystickGetAxis(SDL_Joystick * joystick,
                                                   int axis);
extern Uint8 SDL_JoystickGetHat(SDL_Joystick * joystick,
                                                 int hat);
extern int SDL_JoystickGetBall(SDL_Joystick * joystick,
                                                int ball, int *dx, int *dy);
extern Uint8 SDL_JoystickGetButton(SDL_Joystick * joystick,
                                                    int button);
extern void SDL_JoystickClose(SDL_Joystick * joystick);
struct _SDL_GameController;
typedef struct _SDL_GameController SDL_GameController;
typedef enum
{
    SDL_CONTROLLER_BINDTYPE_NONE = 0,
    SDL_CONTROLLER_BINDTYPE_BUTTON,
    SDL_CONTROLLER_BINDTYPE_AXIS,
    SDL_CONTROLLER_BINDTYPE_HAT
} SDL_GameControllerBindType;
typedef struct SDL_GameControllerButtonBind
{
    SDL_GameControllerBindType bindType;
    union
    {
        int button;
        int axis;
        struct {
            int hat;
            int hat_mask;
        } hat;
    } value;
} SDL_GameControllerButtonBind;
extern int SDL_GameControllerAddMappingsFromRW( SDL_RWops * rw, int freerw );
extern int SDL_GameControllerAddMapping( const char* mappingString );
extern char * SDL_GameControllerMappingForGUID( SDL_JoystickGUID guid );
extern char * SDL_GameControllerMapping( SDL_GameController * gamecontroller );
extern SDL_bool SDL_IsGameController(int joystick_index);
extern const char * SDL_GameControllerNameForIndex(int joystick_index);
extern SDL_GameController * SDL_GameControllerOpen(int joystick_index);
extern const char * SDL_GameControllerName(SDL_GameController *gamecontroller);
extern SDL_bool SDL_GameControllerGetAttached(SDL_GameController *gamecontroller);
extern SDL_Joystick * SDL_GameControllerGetJoystick(SDL_GameController *gamecontroller);
extern int SDL_GameControllerEventState(int state);
extern void SDL_GameControllerUpdate(void);
typedef enum
{
    SDL_CONTROLLER_AXIS_INVALID = -1,
    SDL_CONTROLLER_AXIS_LEFTX,
    SDL_CONTROLLER_AXIS_LEFTY,
    SDL_CONTROLLER_AXIS_RIGHTX,
    SDL_CONTROLLER_AXIS_RIGHTY,
    SDL_CONTROLLER_AXIS_TRIGGERLEFT,
    SDL_CONTROLLER_AXIS_TRIGGERRIGHT,
    SDL_CONTROLLER_AXIS_MAX
} SDL_GameControllerAxis;
extern SDL_GameControllerAxis SDL_GameControllerGetAxisFromString(const char *pchString);
extern const char* SDL_GameControllerGetStringForAxis(SDL_GameControllerAxis axis);
extern SDL_GameControllerButtonBind
SDL_GameControllerGetBindForAxis(SDL_GameController *gamecontroller,
                                 SDL_GameControllerAxis axis);
extern Sint16
SDL_GameControllerGetAxis(SDL_GameController *gamecontroller,
                          SDL_GameControllerAxis axis);
typedef enum
{
    SDL_CONTROLLER_BUTTON_INVALID = -1,
    SDL_CONTROLLER_BUTTON_A,
    SDL_CONTROLLER_BUTTON_B,
    SDL_CONTROLLER_BUTTON_X,
    SDL_CONTROLLER_BUTTON_Y,
    SDL_CONTROLLER_BUTTON_BACK,
    SDL_CONTROLLER_BUTTON_GUIDE,
    SDL_CONTROLLER_BUTTON_START,
    SDL_CONTROLLER_BUTTON_LEFTSTICK,
    SDL_CONTROLLER_BUTTON_RIGHTSTICK,
    SDL_CONTROLLER_BUTTON_LEFTSHOULDER,
    SDL_CONTROLLER_BUTTON_RIGHTSHOULDER,
    SDL_CONTROLLER_BUTTON_DPAD_UP,
    SDL_CONTROLLER_BUTTON_DPAD_DOWN,
    SDL_CONTROLLER_BUTTON_DPAD_LEFT,
    SDL_CONTROLLER_BUTTON_DPAD_RIGHT,
    SDL_CONTROLLER_BUTTON_MAX
} SDL_GameControllerButton;
extern SDL_GameControllerButton SDL_GameControllerGetButtonFromString(const char *pchString);
extern const char* SDL_GameControllerGetStringForButton(SDL_GameControllerButton button);
extern SDL_GameControllerButtonBind
SDL_GameControllerGetBindForButton(SDL_GameController *gamecontroller,
                                   SDL_GameControllerButton button);
extern Uint8 SDL_GameControllerGetButton(SDL_GameController *gamecontroller,
                                                          SDL_GameControllerButton button);
extern void SDL_GameControllerClose(SDL_GameController *gamecontroller);
typedef Sint64 SDL_TouchID;
typedef Sint64 SDL_FingerID;
typedef struct SDL_Finger
{
    SDL_FingerID id;
    float x;
    float y;
    float pressure;
} SDL_Finger;
extern int SDL_GetNumTouchDevices(void);
extern SDL_TouchID SDL_GetTouchDevice(int index);
extern int SDL_GetNumTouchFingers(SDL_TouchID touchID);
extern SDL_Finger * SDL_GetTouchFinger(SDL_TouchID touchID, int index);
typedef Sint64 SDL_GestureID;
extern int SDL_RecordGesture(SDL_TouchID touchId);
extern int SDL_SaveAllDollarTemplates(SDL_RWops *dst);
extern int SDL_SaveDollarTemplate(SDL_GestureID gestureId,SDL_RWops *dst);
extern int SDL_LoadDollarTemplates(SDL_TouchID touchId, SDL_RWops *src);
typedef enum
{
    SDL_FIRSTEVENT = 0,
    SDL_QUIT = 0x100,
    SDL_APP_TERMINATING,
    SDL_APP_LOWMEMORY,
    SDL_APP_WILLENTERBACKGROUND,
    SDL_APP_DIDENTERBACKGROUND,
    SDL_APP_WILLENTERFOREGROUND,
    SDL_APP_DIDENTERFOREGROUND,
    SDL_WINDOWEVENT = 0x200,
    SDL_SYSWMEVENT,
    SDL_KEYDOWN = 0x300,
    SDL_KEYUP,
    SDL_TEXTEDITING,
    SDL_TEXTINPUT,
    SDL_MOUSEMOTION = 0x400,
    SDL_MOUSEBUTTONDOWN,
    SDL_MOUSEBUTTONUP,
    SDL_MOUSEWHEEL,
    SDL_JOYAXISMOTION = 0x600,
    SDL_JOYBALLMOTION,
    SDL_JOYHATMOTION,
    SDL_JOYBUTTONDOWN,
    SDL_JOYBUTTONUP,
    SDL_JOYDEVICEADDED,
    SDL_JOYDEVICEREMOVED,
    SDL_CONTROLLERAXISMOTION = 0x650,
    SDL_CONTROLLERBUTTONDOWN,
    SDL_CONTROLLERBUTTONUP,
    SDL_CONTROLLERDEVICEADDED,
    SDL_CONTROLLERDEVICEREMOVED,
    SDL_CONTROLLERDEVICEREMAPPED,
    SDL_FINGERDOWN = 0x700,
    SDL_FINGERUP,
    SDL_FINGERMOTION,
    SDL_DOLLARGESTURE = 0x800,
    SDL_DOLLARRECORD,
    SDL_MULTIGESTURE,
    SDL_CLIPBOARDUPDATE = 0x900,
    SDL_DROPFILE = 0x1000,
    SDL_RENDER_TARGETS_RESET = 0x2000,
    SDL_USEREVENT = 0x8000,
    SDL_LASTEVENT = 0xFFFF
} SDL_EventType;
typedef struct SDL_CommonEvent
{
    Uint32 type;
    Uint32 timestamp;
} SDL_CommonEvent;
typedef struct SDL_WindowEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint8 event;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint32 data1;
    Sint32 data2;
} SDL_WindowEvent;
typedef struct SDL_KeyboardEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint8 state;
    Uint8 repeat;
    Uint8 padding2;
    Uint8 padding3;
    SDL_Keysym keysym;
} SDL_KeyboardEvent;
typedef struct SDL_TextEditingEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    char text[(32)];
    Sint32 start;
    Sint32 length;
} SDL_TextEditingEvent;
typedef struct SDL_TextInputEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    char text[(32)];
} SDL_TextInputEvent;
typedef struct SDL_MouseMotionEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint32 which;
    Uint32 state;
    Sint32 x;
    Sint32 y;
    Sint32 xrel;
    Sint32 yrel;
} SDL_MouseMotionEvent;
typedef struct SDL_MouseButtonEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint32 which;
    Uint8 button;
    Uint8 state;
    Uint8 clicks;
    Uint8 padding1;
    Sint32 x;
    Sint32 y;
} SDL_MouseButtonEvent;
typedef struct SDL_MouseWheelEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Uint32 which;
    Sint32 x;
    Sint32 y;
} SDL_MouseWheelEvent;
typedef struct SDL_JoyAxisEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 axis;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 value;
    Uint16 padding4;
} SDL_JoyAxisEvent;
typedef struct SDL_JoyBallEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 ball;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 xrel;
    Sint16 yrel;
} SDL_JoyBallEvent;
typedef struct SDL_JoyHatEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 hat;
    Uint8 value;
    Uint8 padding1;
    Uint8 padding2;
} SDL_JoyHatEvent;
typedef struct SDL_JoyButtonEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 button;
    Uint8 state;
    Uint8 padding1;
    Uint8 padding2;
} SDL_JoyButtonEvent;
typedef struct SDL_JoyDeviceEvent
{
    Uint32 type;
    Uint32 timestamp;
    Sint32 which;
} SDL_JoyDeviceEvent;
typedef struct SDL_ControllerAxisEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 axis;
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
    Sint16 value;
    Uint16 padding4;
} SDL_ControllerAxisEvent;
typedef struct SDL_ControllerButtonEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_JoystickID which;
    Uint8 button;
    Uint8 state;
    Uint8 padding1;
    Uint8 padding2;
} SDL_ControllerButtonEvent;
typedef struct SDL_ControllerDeviceEvent
{
    Uint32 type;
    Uint32 timestamp;
    Sint32 which;
} SDL_ControllerDeviceEvent;
typedef struct SDL_TouchFingerEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_TouchID touchId;
    SDL_FingerID fingerId;
    float x;
    float y;
    float dx;
    float dy;
    float pressure;
} SDL_TouchFingerEvent;
typedef struct SDL_MultiGestureEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_TouchID touchId;
    float dTheta;
    float dDist;
    float x;
    float y;
    Uint16 numFingers;
    Uint16 padding;
} SDL_MultiGestureEvent;
typedef struct SDL_DollarGestureEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_TouchID touchId;
    SDL_GestureID gestureId;
    Uint32 numFingers;
    float error;
    float x;
    float y;
} SDL_DollarGestureEvent;
typedef struct SDL_DropEvent
{
    Uint32 type;
    Uint32 timestamp;
    char *file;
} SDL_DropEvent;
typedef struct SDL_QuitEvent
{
    Uint32 type;
    Uint32 timestamp;
} SDL_QuitEvent;
typedef struct SDL_OSEvent
{
    Uint32 type;
    Uint32 timestamp;
} SDL_OSEvent;
typedef struct SDL_UserEvent
{
    Uint32 type;
    Uint32 timestamp;
    Uint32 windowID;
    Sint32 code;
    void *data1;
    void *data2;
} SDL_UserEvent;
struct SDL_SysWMmsg;
typedef struct SDL_SysWMmsg SDL_SysWMmsg;
typedef struct SDL_SysWMEvent
{
    Uint32 type;
    Uint32 timestamp;
    SDL_SysWMmsg *msg;
} SDL_SysWMEvent;
typedef union SDL_Event
{
    Uint32 type;
    SDL_CommonEvent common;
    SDL_WindowEvent window;
    SDL_KeyboardEvent key;
    SDL_TextEditingEvent edit;
    SDL_TextInputEvent text;
    SDL_MouseMotionEvent motion;
    SDL_MouseButtonEvent button;
    SDL_MouseWheelEvent wheel;
    SDL_JoyAxisEvent jaxis;
    SDL_JoyBallEvent jball;
    SDL_JoyHatEvent jhat;
    SDL_JoyButtonEvent jbutton;
    SDL_JoyDeviceEvent jdevice;
    SDL_ControllerAxisEvent caxis;
    SDL_ControllerButtonEvent cbutton;
    SDL_ControllerDeviceEvent cdevice;
    SDL_QuitEvent quit;
    SDL_UserEvent user;
    SDL_SysWMEvent syswm;
    SDL_TouchFingerEvent tfinger;
    SDL_MultiGestureEvent mgesture;
    SDL_DollarGestureEvent dgesture;
    SDL_DropEvent drop;
    Uint8 padding[56];
} SDL_Event;
extern void SDL_PumpEvents(void);
typedef enum
{
    SDL_ADDEVENT,
    SDL_PEEKEVENT,
    SDL_GETEVENT
} SDL_eventaction;
extern int SDL_PeepEvents(SDL_Event * events, int numevents,
                                           SDL_eventaction action,
                                           Uint32 minType, Uint32 maxType);
extern SDL_bool SDL_HasEvent(Uint32 type);
extern SDL_bool SDL_HasEvents(Uint32 minType, Uint32 maxType);
extern void SDL_FlushEvent(Uint32 type);
extern void SDL_FlushEvents(Uint32 minType, Uint32 maxType);
extern int SDL_PollEvent(SDL_Event * event);
extern int SDL_WaitEvent(SDL_Event * event);
extern int SDL_WaitEventTimeout(SDL_Event * event,
                                                 int timeout);
extern int SDL_PushEvent(SDL_Event * event);
typedef int ( * SDL_EventFilter) (void *userdata, SDL_Event * event);
extern void SDL_SetEventFilter(SDL_EventFilter filter,
                                                void *userdata);
extern SDL_bool SDL_GetEventFilter(SDL_EventFilter * filter,
                                                    void **userdata);
extern void SDL_AddEventWatch(SDL_EventFilter filter,
                                               void *userdata);
extern void SDL_DelEventWatch(SDL_EventFilter filter,
                                               void *userdata);
extern void SDL_FilterEvents(SDL_EventFilter filter,
                                              void *userdata);
extern Uint8 SDL_EventState(Uint32 type, int state);
extern Uint32 SDL_RegisterEvents(int numevents);
extern char * SDL_GetBasePath(void);
extern char * SDL_GetPrefPath(const char *org, const char *app);
struct _SDL_Haptic;
typedef struct _SDL_Haptic SDL_Haptic;
typedef struct SDL_HapticDirection
{
    Uint8 type;
    Sint32 dir[3];
} SDL_HapticDirection;
typedef struct SDL_HapticConstant
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Sint16 level;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticConstant;
typedef struct SDL_HapticPeriodic
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Uint16 period;
    Sint16 magnitude;
    Sint16 offset;
    Uint16 phase;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticPeriodic;
typedef struct SDL_HapticCondition
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Uint16 right_sat[3];
    Uint16 left_sat[3];
    Sint16 right_coeff[3];
    Sint16 left_coeff[3];
    Uint16 deadband[3];
    Sint16 center[3];
} SDL_HapticCondition;
typedef struct SDL_HapticRamp
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Sint16 start;
    Sint16 end;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticRamp;
typedef struct SDL_HapticLeftRight
{
    Uint16 type;
    Uint32 length;
    Uint16 large_magnitude;
    Uint16 small_magnitude;
} SDL_HapticLeftRight;
typedef struct SDL_HapticCustom
{
    Uint16 type;
    SDL_HapticDirection direction;
    Uint32 length;
    Uint16 delay;
    Uint16 button;
    Uint16 interval;
    Uint8 channels;
    Uint16 period;
    Uint16 samples;
    Uint16 *data;
    Uint16 attack_length;
    Uint16 attack_level;
    Uint16 fade_length;
    Uint16 fade_level;
} SDL_HapticCustom;
typedef union SDL_HapticEffect
{
    Uint16 type;
    SDL_HapticConstant constant;
    SDL_HapticPeriodic periodic;
    SDL_HapticCondition condition;
    SDL_HapticRamp ramp;
    SDL_HapticLeftRight leftright;
    SDL_HapticCustom custom;
} SDL_HapticEffect;
extern int SDL_NumHaptics(void);
extern const char * SDL_HapticName(int device_index);
extern SDL_Haptic * SDL_HapticOpen(int device_index);
extern int SDL_HapticOpened(int device_index);
extern int SDL_HapticIndex(SDL_Haptic * haptic);
extern int SDL_MouseIsHaptic(void);
extern SDL_Haptic * SDL_HapticOpenFromMouse(void);
extern int SDL_JoystickIsHaptic(SDL_Joystick * joystick);
extern SDL_Haptic * SDL_HapticOpenFromJoystick(SDL_Joystick *
                                                               joystick);
extern void SDL_HapticClose(SDL_Haptic * haptic);
extern int SDL_HapticNumEffects(SDL_Haptic * haptic);
extern int SDL_HapticNumEffectsPlaying(SDL_Haptic * haptic);
extern unsigned int SDL_HapticQuery(SDL_Haptic * haptic);
extern int SDL_HapticNumAxes(SDL_Haptic * haptic);
extern int SDL_HapticEffectSupported(SDL_Haptic * haptic,
                                                      SDL_HapticEffect *
                                                      effect);
extern int SDL_HapticNewEffect(SDL_Haptic * haptic,
                                                SDL_HapticEffect * effect);
extern int SDL_HapticUpdateEffect(SDL_Haptic * haptic,
                                                   int effect,
                                                   SDL_HapticEffect * data);
extern int SDL_HapticRunEffect(SDL_Haptic * haptic,
                                                int effect,
                                                Uint32 iterations);
extern int SDL_HapticStopEffect(SDL_Haptic * haptic,
                                                 int effect);
extern void SDL_HapticDestroyEffect(SDL_Haptic * haptic,
                                                     int effect);
extern int SDL_HapticGetEffectStatus(SDL_Haptic * haptic,
                                                      int effect);
extern int SDL_HapticSetGain(SDL_Haptic * haptic, int gain);
extern int SDL_HapticSetAutocenter(SDL_Haptic * haptic,
                                                    int autocenter);
extern int SDL_HapticPause(SDL_Haptic * haptic);
extern int SDL_HapticUnpause(SDL_Haptic * haptic);
extern int SDL_HapticStopAll(SDL_Haptic * haptic);
extern int SDL_HapticRumbleSupported(SDL_Haptic * haptic);
extern int SDL_HapticRumbleInit(SDL_Haptic * haptic);
extern int SDL_HapticRumblePlay(SDL_Haptic * haptic, float strength, Uint32 length );
extern int SDL_HapticRumbleStop(SDL_Haptic * haptic);
typedef enum
{
    SDL_HINT_DEFAULT,
    SDL_HINT_NORMAL,
    SDL_HINT_OVERRIDE
} SDL_HintPriority;
extern SDL_bool SDL_SetHintWithPriority(const char *name,
                                                         const char *value,
                                                         SDL_HintPriority priority);
extern SDL_bool SDL_SetHint(const char *name,
                                             const char *value);
extern const char * SDL_GetHint(const char *name);
typedef void (*SDL_HintCallback)(void *userdata, const char *name, const char *oldValue, const char *newValue);
extern void SDL_AddHintCallback(const char *name,
                                                 SDL_HintCallback callback,
                                                 void *userdata);
extern void SDL_DelHintCallback(const char *name,
                                                 SDL_HintCallback callback,
                                                 void *userdata);
extern void SDL_ClearHints(void);
extern void * SDL_LoadObject(const char *sofile);
extern void * SDL_LoadFunction(void *handle,
                                               const char *name);
extern void SDL_UnloadObject(void *handle);
enum
{
    SDL_LOG_CATEGORY_APPLICATION,
    SDL_LOG_CATEGORY_ERROR,
    SDL_LOG_CATEGORY_ASSERT,
    SDL_LOG_CATEGORY_SYSTEM,
    SDL_LOG_CATEGORY_AUDIO,
    SDL_LOG_CATEGORY_VIDEO,
    SDL_LOG_CATEGORY_RENDER,
    SDL_LOG_CATEGORY_INPUT,
    SDL_LOG_CATEGORY_TEST,
    SDL_LOG_CATEGORY_RESERVED1,
    SDL_LOG_CATEGORY_RESERVED2,
    SDL_LOG_CATEGORY_RESERVED3,
    SDL_LOG_CATEGORY_RESERVED4,
    SDL_LOG_CATEGORY_RESERVED5,
    SDL_LOG_CATEGORY_RESERVED6,
    SDL_LOG_CATEGORY_RESERVED7,
    SDL_LOG_CATEGORY_RESERVED8,
    SDL_LOG_CATEGORY_RESERVED9,
    SDL_LOG_CATEGORY_RESERVED10,
    SDL_LOG_CATEGORY_CUSTOM
};
typedef enum
{
    SDL_LOG_PRIORITY_VERBOSE = 1,
    SDL_LOG_PRIORITY_DEBUG,
    SDL_LOG_PRIORITY_INFO,
    SDL_LOG_PRIORITY_WARN,
    SDL_LOG_PRIORITY_ERROR,
    SDL_LOG_PRIORITY_CRITICAL,
    SDL_NUM_LOG_PRIORITIES
} SDL_LogPriority;
extern void SDL_LogSetAllPriority(SDL_LogPriority priority);
extern void SDL_LogSetPriority(int category,
                                                SDL_LogPriority priority);
extern SDL_LogPriority SDL_LogGetPriority(int category);
extern void SDL_LogResetPriorities(void);
extern void SDL_Log(const char *fmt, ...);
extern void SDL_LogVerbose(int category, const char *fmt, ...);
extern void SDL_LogDebug(int category, const char *fmt, ...);
extern void SDL_LogInfo(int category, const char *fmt, ...);
extern void SDL_LogWarn(int category, const char *fmt, ...);
extern void SDL_LogError(int category, const char *fmt, ...);
extern void SDL_LogCritical(int category, const char *fmt, ...);
extern void SDL_LogMessage(int category,
                                            SDL_LogPriority priority,
                                            const char *fmt, ...);

typedef void (*SDL_LogOutputFunction)(void *userdata, int category, SDL_LogPriority priority, const char *message);
extern void SDL_LogGetOutputFunction(SDL_LogOutputFunction *callback, void **userdata);
extern void SDL_LogSetOutputFunction(SDL_LogOutputFunction callback, void *userdata);
typedef enum
{
    SDL_MESSAGEBOX_ERROR = 0x00000010,
    SDL_MESSAGEBOX_WARNING = 0x00000020,
    SDL_MESSAGEBOX_INFORMATION = 0x00000040
} SDL_MessageBoxFlags;
typedef enum
{
    SDL_MESSAGEBOX_BUTTON_RETURNKEY_DEFAULT = 0x00000001,
    SDL_MESSAGEBOX_BUTTON_ESCAPEKEY_DEFAULT = 0x00000002
} SDL_MessageBoxButtonFlags;
typedef struct
{
    Uint32 flags;
    int buttonid;
    const char * text;
} SDL_MessageBoxButtonData;
typedef struct
{
    Uint8 r, g, b;
} SDL_MessageBoxColor;
typedef enum
{
    SDL_MESSAGEBOX_COLOR_BACKGROUND,
    SDL_MESSAGEBOX_COLOR_TEXT,
    SDL_MESSAGEBOX_COLOR_BUTTON_BORDER,
    SDL_MESSAGEBOX_COLOR_BUTTON_BACKGROUND,
    SDL_MESSAGEBOX_COLOR_BUTTON_SELECTED,
    SDL_MESSAGEBOX_COLOR_MAX
} SDL_MessageBoxColorType;
typedef struct
{
    SDL_MessageBoxColor colors[SDL_MESSAGEBOX_COLOR_MAX];
} SDL_MessageBoxColorScheme;
typedef struct
{
    Uint32 flags;
    SDL_Window *window;
    const char *title;
    const char *message;
    int numbuttons;
    const SDL_MessageBoxButtonData *buttons;
    const SDL_MessageBoxColorScheme *colorScheme;
} SDL_MessageBoxData;
extern int SDL_ShowMessageBox(const SDL_MessageBoxData *messageboxdata, int *buttonid);
extern int SDL_ShowSimpleMessageBox(Uint32 flags, const char *title, const char *message, SDL_Window *window);
typedef enum
{
    SDL_POWERSTATE_UNKNOWN,
    SDL_POWERSTATE_ON_BATTERY,
    SDL_POWERSTATE_NO_BATTERY,
    SDL_POWERSTATE_CHARGING,
    SDL_POWERSTATE_CHARGED
} SDL_PowerState;
extern SDL_PowerState SDL_GetPowerInfo(int *secs, int *pct);
typedef enum
{
    SDL_RENDERER_SOFTWARE = 0x00000001,
    SDL_RENDERER_ACCELERATED = 0x00000002,
    SDL_RENDERER_PRESENTVSYNC = 0x00000004,
    SDL_RENDERER_TARGETTEXTURE = 0x00000008
} SDL_RendererFlags;
typedef struct SDL_RendererInfo
{
    const char *name;
    Uint32 flags;
    Uint32 num_texture_formats;
    Uint32 texture_formats[16];
    int max_texture_width;
    int max_texture_height;
} SDL_RendererInfo;
typedef enum
{
    SDL_TEXTUREACCESS_STATIC,
    SDL_TEXTUREACCESS_STREAMING,
    SDL_TEXTUREACCESS_TARGET
} SDL_TextureAccess;
typedef enum
{
    SDL_TEXTUREMODULATE_NONE = 0x00000000,
    SDL_TEXTUREMODULATE_COLOR = 0x00000001,
    SDL_TEXTUREMODULATE_ALPHA = 0x00000002
} SDL_TextureModulate;
typedef enum
{
    SDL_FLIP_NONE = 0x00000000,
    SDL_FLIP_HORIZONTAL = 0x00000001,
    SDL_FLIP_VERTICAL = 0x00000002
} SDL_RendererFlip;
struct SDL_Renderer;
typedef struct SDL_Renderer SDL_Renderer;
struct SDL_Texture;
typedef struct SDL_Texture SDL_Texture;
extern int SDL_GetNumRenderDrivers(void);
extern int SDL_GetRenderDriverInfo(int index,
                                                    SDL_RendererInfo * info);
extern int SDL_CreateWindowAndRenderer(
                                int width, int height, Uint32 window_flags,
                                SDL_Window **window, SDL_Renderer **renderer);
extern SDL_Renderer * SDL_CreateRenderer(SDL_Window * window,
                                               int index, Uint32 flags);
extern SDL_Renderer * SDL_CreateSoftwareRenderer(SDL_Surface * surface);
extern SDL_Renderer * SDL_GetRenderer(SDL_Window * window);
extern int SDL_GetRendererInfo(SDL_Renderer * renderer,
                                                SDL_RendererInfo * info);
extern int SDL_GetRendererOutputSize(SDL_Renderer * renderer,
                                                      int *w, int *h);
extern SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
                                                        Uint32 format,
                                                        int access, int w,
                                                        int h);
extern SDL_Texture * SDL_CreateTextureFromSurface(SDL_Renderer * renderer, SDL_Surface * surface);
extern int SDL_QueryTexture(SDL_Texture * texture,
                                             Uint32 * format, int *access,
                                             int *w, int *h);
extern int SDL_SetTextureColorMod(SDL_Texture * texture,
                                                   Uint8 r, Uint8 g, Uint8 b);
extern int SDL_GetTextureColorMod(SDL_Texture * texture,
                                                   Uint8 * r, Uint8 * g,
                                                   Uint8 * b);
extern int SDL_SetTextureAlphaMod(SDL_Texture * texture,
                                                   Uint8 alpha);
extern int SDL_GetTextureAlphaMod(SDL_Texture * texture,
                                                   Uint8 * alpha);
extern int SDL_SetTextureBlendMode(SDL_Texture * texture,
                                                    SDL_BlendMode blendMode);
extern int SDL_GetTextureBlendMode(SDL_Texture * texture,
                                                    SDL_BlendMode *blendMode);
extern int SDL_UpdateTexture(SDL_Texture * texture,
                                              const SDL_Rect * rect,
                                              const void *pixels, int pitch);
extern int SDL_UpdateYUVTexture(SDL_Texture * texture,
                                                 const SDL_Rect * rect,
                                                 const Uint8 *Yplane, int Ypitch,
                                                 const Uint8 *Uplane, int Upitch,
                                                 const Uint8 *Vplane, int Vpitch);
extern int SDL_LockTexture(SDL_Texture * texture,
                                            const SDL_Rect * rect,
                                            void **pixels, int *pitch);
extern void SDL_UnlockTexture(SDL_Texture * texture);
extern SDL_bool SDL_RenderTargetSupported(SDL_Renderer *renderer);
extern int SDL_SetRenderTarget(SDL_Renderer *renderer,
                                                SDL_Texture *texture);
extern SDL_Texture * SDL_GetRenderTarget(SDL_Renderer *renderer);
extern int SDL_RenderSetLogicalSize(SDL_Renderer * renderer, int w, int h);
extern void SDL_RenderGetLogicalSize(SDL_Renderer * renderer, int *w, int *h);
extern int SDL_RenderSetViewport(SDL_Renderer * renderer,
                                                  const SDL_Rect * rect);
extern void SDL_RenderGetViewport(SDL_Renderer * renderer,
                                                   SDL_Rect * rect);
extern int SDL_RenderSetClipRect(SDL_Renderer * renderer,
                                                  const SDL_Rect * rect);
extern void SDL_RenderGetClipRect(SDL_Renderer * renderer,
                                                   SDL_Rect * rect);
extern int SDL_RenderSetScale(SDL_Renderer * renderer,
                                               float scaleX, float scaleY);
extern void SDL_RenderGetScale(SDL_Renderer * renderer,
                                               float *scaleX, float *scaleY);
extern int SDL_SetRenderDrawColor(SDL_Renderer * renderer,
                                           Uint8 r, Uint8 g, Uint8 b,
                                           Uint8 a);
extern int SDL_GetRenderDrawColor(SDL_Renderer * renderer,
                                           Uint8 * r, Uint8 * g, Uint8 * b,
                                           Uint8 * a);
extern int SDL_SetRenderDrawBlendMode(SDL_Renderer * renderer,
                                                       SDL_BlendMode blendMode);
extern int SDL_GetRenderDrawBlendMode(SDL_Renderer * renderer,
                                                       SDL_BlendMode *blendMode);
extern int SDL_RenderClear(SDL_Renderer * renderer);
extern int SDL_RenderDrawPoint(SDL_Renderer * renderer,
                                                int x, int y);
extern int SDL_RenderDrawPoints(SDL_Renderer * renderer,
                                                 const SDL_Point * points,
                                                 int count);
extern int SDL_RenderDrawLine(SDL_Renderer * renderer,
                                               int x1, int y1, int x2, int y2);
extern int SDL_RenderDrawLines(SDL_Renderer * renderer,
                                                const SDL_Point * points,
                                                int count);
extern int SDL_RenderDrawRect(SDL_Renderer * renderer,
                                               const SDL_Rect * rect);
extern int SDL_RenderDrawRects(SDL_Renderer * renderer,
                                                const SDL_Rect * rects,
                                                int count);
extern int SDL_RenderFillRect(SDL_Renderer * renderer,
                                               const SDL_Rect * rect);
extern int SDL_RenderFillRects(SDL_Renderer * renderer,
                                                const SDL_Rect * rects,
                                                int count);
extern int SDL_RenderCopy(SDL_Renderer * renderer,
                                           SDL_Texture * texture,
                                           const SDL_Rect * srcrect,
                                           const SDL_Rect * dstrect);
extern int SDL_RenderCopyEx(SDL_Renderer * renderer,
                                           SDL_Texture * texture,
                                           const SDL_Rect * srcrect,
                                           const SDL_Rect * dstrect,
                                           const double angle,
                                           const SDL_Point *center,
                                           const SDL_RendererFlip flip);
extern int SDL_RenderReadPixels(SDL_Renderer * renderer,
                                                 const SDL_Rect * rect,
                                                 Uint32 format,
                                                 void *pixels, int pitch);
extern void SDL_RenderPresent(SDL_Renderer * renderer);
extern void SDL_DestroyTexture(SDL_Texture * texture);
extern void SDL_DestroyRenderer(SDL_Renderer * renderer);
extern int SDL_GL_BindTexture(SDL_Texture *texture, float *texw, float *texh);
extern int SDL_GL_UnbindTexture(SDL_Texture *texture);
extern Uint32 SDL_GetTicks(void);
extern Uint64 SDL_GetPerformanceCounter(void);
extern Uint64 SDL_GetPerformanceFrequency(void);
extern void SDL_Delay(Uint32 ms);
typedef Uint32 ( * SDL_TimerCallback) (Uint32 interval, void *param);
typedef int SDL_TimerID;
extern SDL_TimerID SDL_AddTimer(Uint32 interval,
                                                 SDL_TimerCallback callback,
                                                 void *param);
extern SDL_bool SDL_RemoveTimer(SDL_TimerID id);
typedef struct SDL_version
{
    Uint8 major;
    Uint8 minor;
    Uint8 patch;
} SDL_version;
extern void SDL_GetVersion(SDL_version * ver);
extern const char * SDL_GetRevision(void);
extern int SDL_GetRevisionNumber(void);
extern int SDL_Init(Uint32 flags);
extern int SDL_InitSubSystem(Uint32 flags);
extern void SDL_QuitSubSystem(Uint32 flags);
extern Uint32 SDL_WasInit(Uint32 flags);
extern void SDL_Quit(void);
