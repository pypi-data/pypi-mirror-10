
#include <stdio.h>
#include <stddef.h>
#include <stdarg.h>
#include <errno.h>
#include <sys/types.h>   /* XXX for ssize_t on some platforms */

#ifdef _WIN32
#  include <Windows.h>
#  define snprintf _snprintf
typedef __int8 int8_t;
typedef __int16 int16_t;
typedef __int32 int32_t;
typedef __int64 int64_t;
typedef unsigned __int8 uint8_t;
typedef unsigned __int16 uint16_t;
typedef unsigned __int32 uint32_t;
typedef unsigned __int64 uint64_t;
typedef SSIZE_T ssize_t;
typedef unsigned char _Bool;
#else
#  include <stdint.h>
#endif


#include <openssl/bn.h>
#include <openssl/ec.h>
#include <openssl/evp.h>
#include <openssl/hmac.h>
#include <openssl/ecdsa.h>

#define BN_num_bytes(a) ((BN_num_bits(a)+7)/8)


int bn_num_bytes(BIGNUM * a){
    return BN_num_bytes(a);
}

int bn_is_odd(BIGNUM * a){
    return BN_is_odd(a);
}

size_t hmac_ctx_size(void){
    return sizeof(HMAC_CTX);
}


extern void ERR_load_crypto_strings(void);
extern void OPENSSL_config(void*);
extern void ERR_free_strings(void);

void init_ciphers(void){

    /* Load the human readable error strings for libcrypto */
    ERR_load_crypto_strings();

    /* Load all digest and cipher algorithms */
    OpenSSL_add_all_algorithms();

    /* Load config file, and other important initialisation */
    OPENSSL_config(NULL);

}

void cleanup_ciphers(void){

    /* Removes all digests and ciphers */
    EVP_cleanup();

    /* if you omit the next, a small leak may be left when you make use of the BIO (low level API) for e.g. base64 transformations */
    CRYPTO_cleanup_all_ex_data();

    /* Remove error strings */
    ERR_free_strings();

}


static void _cffi_check__EC_builtin_curve(EC_builtin_curve *p)
{
  /* only to generate compile-time warnings or errors */
  (void)((p->nid) << 1);
  { char const * *tmp = &p->comment; (void)tmp; }
}
ssize_t _cffi_layout__EC_builtin_curve(ssize_t i)
{
  struct _cffi_aligncheck { char x; EC_builtin_curve y; };
  static ssize_t nums[] = {
    sizeof(EC_builtin_curve),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(EC_builtin_curve, nid),
    sizeof(((EC_builtin_curve *)0)->nid),
    offsetof(EC_builtin_curve, comment),
    sizeof(((EC_builtin_curve *)0)->comment),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check__EC_builtin_curve(0);
}

static void _cffi_check__HMAC_CTX(HMAC_CTX *p)
{
  /* only to generate compile-time warnings or errors */
}
ssize_t _cffi_layout__HMAC_CTX(ssize_t i)
{
  struct _cffi_aligncheck { char x; HMAC_CTX y; };
  static ssize_t nums[] = {
    sizeof(HMAC_CTX),
    offsetof(struct _cffi_aligncheck, y),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check__HMAC_CTX(0);
}

int _cffi_e_enum_foo(char *out_error)
{
  if ((POINT_CONVERSION_COMPRESSED) < 0 || (unsigned long)(POINT_CONVERSION_COMPRESSED) != 2UL) {
    char buf[64];
    if ((POINT_CONVERSION_COMPRESSED) < 0)
        snprintf(buf, 63, "%ld", (long)(POINT_CONVERSION_COMPRESSED));
    else
        snprintf(buf, 63, "%lu", (unsigned long)(POINT_CONVERSION_COMPRESSED));
    snprintf(out_error, 255, "%s has the real value %s, not %s",
            "POINT_CONVERSION_COMPRESSED", buf, "2");
    return -1;
  }
  if ((POINT_CONVERSION_UNCOMPRESSED) < 0 || (unsigned long)(POINT_CONVERSION_UNCOMPRESSED) != 4UL) {
    char buf[64];
    if ((POINT_CONVERSION_UNCOMPRESSED) < 0)
        snprintf(buf, 63, "%ld", (long)(POINT_CONVERSION_UNCOMPRESSED));
    else
        snprintf(buf, 63, "%lu", (unsigned long)(POINT_CONVERSION_UNCOMPRESSED));
    snprintf(out_error, 255, "%s has the real value %s, not %s",
            "POINT_CONVERSION_UNCOMPRESSED", buf, "4");
    return -1;
  }
  if ((POINT_CONVERSION_HYBRID) < 0 || (unsigned long)(POINT_CONVERSION_HYBRID) != 6UL) {
    char buf[64];
    if ((POINT_CONVERSION_HYBRID) < 0)
        snprintf(buf, 63, "%ld", (long)(POINT_CONVERSION_HYBRID));
    else
        snprintf(buf, 63, "%lu", (unsigned long)(POINT_CONVERSION_HYBRID));
    snprintf(out_error, 255, "%s has the real value %s, not %s",
            "POINT_CONVERSION_HYBRID", buf, "6");
    return -1;
  }
  return 0;
}

void _cffi_f_BN_CTX_free(BN_CTX * x0)
{
  BN_CTX_free(x0);
}

BN_CTX * _cffi_f_BN_CTX_new(void)
{
  return BN_CTX_new();
}

int _cffi_f_BN_add(BIGNUM * x0, BIGNUM const * x1, BIGNUM const * x2)
{
  return BN_add(x0, x1, x2);
}

BIGNUM * _cffi_f_BN_bin2bn(unsigned char const * x0, int x1, BIGNUM * x2)
{
  return BN_bin2bn(x0, x1, x2);
}

int _cffi_f_BN_bn2bin(BIGNUM const * x0, unsigned char * x1)
{
  return BN_bn2bin(x0, x1);
}

char * _cffi_f_BN_bn2dec(BIGNUM const * x0)
{
  return BN_bn2dec(x0);
}

char * _cffi_f_BN_bn2hex(BIGNUM const * x0)
{
  return BN_bn2hex(x0);
}

void _cffi_f_BN_clear_free(BIGNUM * x0)
{
  BN_clear_free(x0);
}

int _cffi_f_BN_cmp(BIGNUM const * x0, BIGNUM const * x1)
{
  return BN_cmp(x0, x1);
}

BIGNUM * _cffi_f_BN_copy(BIGNUM * x0, BIGNUM const * x1)
{
  return BN_copy(x0, x1);
}

int _cffi_f_BN_dec2bn(BIGNUM * * x0, char const * x1)
{
  return BN_dec2bn(x0, x1);
}

int _cffi_f_BN_div(BIGNUM * x0, BIGNUM * x1, BIGNUM const * x2, BIGNUM const * x3, BN_CTX * x4)
{
  return BN_div(x0, x1, x2, x3, x4);
}

int _cffi_f_BN_exp(BIGNUM * x0, BIGNUM const * x1, BIGNUM const * x2, BN_CTX * x3)
{
  return BN_exp(x0, x1, x2, x3);
}

int _cffi_f_BN_generate_prime_ex(BIGNUM * x0, int x1, int x2, BIGNUM const * x3, BIGNUM const * x4, BN_GENCB * x5)
{
  return BN_generate_prime_ex(x0, x1, x2, x3, x4, x5);
}

int _cffi_f_BN_hex2bn(BIGNUM * * x0, char const * x1)
{
  return BN_hex2bn(x0, x1);
}

void _cffi_f_BN_init(BIGNUM * x0)
{
  BN_init(x0);
}

int _cffi_f_BN_is_bit_set(BIGNUM const * x0, int x1)
{
  return BN_is_bit_set(x0, x1);
}

int _cffi_f_BN_is_prime_ex(BIGNUM const * x0, int x1, BN_CTX * x2, BN_GENCB * x3)
{
  return BN_is_prime_ex(x0, x1, x2, x3);
}

int _cffi_f_BN_mod_add(BIGNUM * x0, BIGNUM * x1, BIGNUM * x2, BIGNUM const * x3, BN_CTX * x4)
{
  return BN_mod_add(x0, x1, x2, x3, x4);
}

int _cffi_f_BN_mod_exp(BIGNUM * x0, BIGNUM const * x1, BIGNUM const * x2, BIGNUM const * x3, BN_CTX * x4)
{
  return BN_mod_exp(x0, x1, x2, x3, x4);
}

BIGNUM * _cffi_f_BN_mod_inverse(BIGNUM * x0, BIGNUM const * x1, BIGNUM const * x2, BN_CTX * x3)
{
  return BN_mod_inverse(x0, x1, x2, x3);
}

int _cffi_f_BN_mod_mul(BIGNUM * x0, BIGNUM * x1, BIGNUM * x2, BIGNUM const * x3, BN_CTX * x4)
{
  return BN_mod_mul(x0, x1, x2, x3, x4);
}

int _cffi_f_BN_mod_sub(BIGNUM * x0, BIGNUM * x1, BIGNUM * x2, BIGNUM const * x3, BN_CTX * x4)
{
  return BN_mod_sub(x0, x1, x2, x3, x4);
}

int _cffi_f_BN_mul(BIGNUM * x0, BIGNUM const * x1, BIGNUM const * x2, BN_CTX * x3)
{
  return BN_mul(x0, x1, x2, x3);
}

BIGNUM * _cffi_f_BN_new(void)
{
  return BN_new();
}

int _cffi_f_BN_nnmod(BIGNUM * x0, BIGNUM const * x1, BIGNUM const * x2, BN_CTX * x3)
{
  return BN_nnmod(x0, x1, x2, x3);
}

int _cffi_f_BN_num_bits(BIGNUM const * x0)
{
  return BN_num_bits(x0);
}

int _cffi_f_BN_rand_range(BIGNUM * x0, BIGNUM const * x1)
{
  return BN_rand_range(x0, x1);
}

void _cffi_f_BN_set_negative(BIGNUM * x0, int x1)
{
  BN_set_negative(x0, x1);
}

int _cffi_f_BN_set_word(BIGNUM * x0, unsigned int x1)
{
  return BN_set_word(x0, x1);
}

int _cffi_f_BN_sub(BIGNUM * x0, BIGNUM const * x1, BIGNUM const * x2)
{
  return BN_sub(x0, x1, x2);
}

void _cffi_f_BN_swap(BIGNUM * x0, BIGNUM * x1)
{
  BN_swap(x0, x1);
}

int _cffi_f_CRYPTO_memcmp(void const * x0, void const * x1, size_t x2)
{
  return CRYPTO_memcmp(x0, x1, x2);
}

void _cffi_f_ECDSA_SIG_free(ECDSA_SIG * x0)
{
  ECDSA_SIG_free(x0);
}

ECDSA_SIG * _cffi_f_ECDSA_SIG_new(void)
{
  return ECDSA_SIG_new();
}

ECDSA_SIG * _cffi_f_ECDSA_do_sign(unsigned char const * x0, int x1, EC_KEY * x2)
{
  return ECDSA_do_sign(x0, x1, x2);
}

ECDSA_SIG * _cffi_f_ECDSA_do_sign_ex(unsigned char const * x0, int x1, BIGNUM const * x2, BIGNUM const * x3, EC_KEY * x4)
{
  return ECDSA_do_sign_ex(x0, x1, x2, x3, x4);
}

int _cffi_f_ECDSA_do_verify(unsigned char const * x0, int x1, ECDSA_SIG const * x2, EC_KEY * x3)
{
  return ECDSA_do_verify(x0, x1, x2, x3);
}

int _cffi_f_ECDSA_sign_setup(EC_KEY * x0, BN_CTX * x1, BIGNUM * * x2, BIGNUM * * x3)
{
  return ECDSA_sign_setup(x0, x1, x2, x3);
}

int _cffi_f_ECDSA_size(EC_KEY const * x0)
{
  return ECDSA_size(x0);
}

void _cffi_f_EC_GROUP_clear_free(EC_GROUP * x0)
{
  EC_GROUP_clear_free(x0);
}

int _cffi_f_EC_GROUP_cmp(EC_GROUP const * x0, EC_GROUP const * x1, BN_CTX * x2)
{
  return EC_GROUP_cmp(x0, x1, x2);
}

void _cffi_f_EC_GROUP_free(EC_GROUP * x0)
{
  EC_GROUP_free(x0);
}

EC_POINT const * _cffi_f_EC_GROUP_get0_generator(EC_GROUP const * x0)
{
  return EC_GROUP_get0_generator(x0);
}

int _cffi_f_EC_GROUP_get_cofactor(EC_GROUP const * x0, BIGNUM * x1, BN_CTX * x2)
{
  return EC_GROUP_get_cofactor(x0, x1, x2);
}

int _cffi_f_EC_GROUP_get_curve_GFp(EC_GROUP const * x0, BIGNUM * x1, BIGNUM * x2, BIGNUM * x3, BN_CTX * x4)
{
  return EC_GROUP_get_curve_GFp(x0, x1, x2, x3, x4);
}

int _cffi_f_EC_GROUP_get_curve_name(EC_GROUP const * x0)
{
  return EC_GROUP_get_curve_name(x0);
}

int _cffi_f_EC_GROUP_get_order(EC_GROUP const * x0, BIGNUM * x1, BN_CTX * x2)
{
  return EC_GROUP_get_order(x0, x1, x2);
}

int _cffi_f_EC_GROUP_have_precompute_mult(EC_GROUP const * x0)
{
  return EC_GROUP_have_precompute_mult(x0);
}

EC_GROUP * _cffi_f_EC_GROUP_new_by_curve_name(int x0)
{
  return EC_GROUP_new_by_curve_name(x0);
}

int _cffi_f_EC_GROUP_precompute_mult(EC_GROUP * x0, BN_CTX * x1)
{
  return EC_GROUP_precompute_mult(x0, x1);
}

void _cffi_f_EC_KEY_free(EC_KEY * x0)
{
  EC_KEY_free(x0);
}

EC_KEY * _cffi_f_EC_KEY_new(void)
{
  return EC_KEY_new();
}

int _cffi_f_EC_KEY_set_group(EC_KEY * x0, EC_GROUP const * x1)
{
  return EC_KEY_set_group(x0, x1);
}

int _cffi_f_EC_KEY_set_private_key(EC_KEY * x0, BIGNUM const * x1)
{
  return EC_KEY_set_private_key(x0, x1);
}

int _cffi_f_EC_KEY_set_public_key(EC_KEY * x0, EC_POINT const * x1)
{
  return EC_KEY_set_public_key(x0, x1);
}

int _cffi_f_EC_POINT_add(EC_GROUP const * x0, EC_POINT * x1, EC_POINT const * x2, EC_POINT const * x3, BN_CTX * x4)
{
  return EC_POINT_add(x0, x1, x2, x3, x4);
}

void _cffi_f_EC_POINT_clear_free(EC_POINT * x0)
{
  EC_POINT_clear_free(x0);
}

int _cffi_f_EC_POINT_cmp(EC_GROUP const * x0, EC_POINT const * x1, EC_POINT const * x2, BN_CTX * x3)
{
  return EC_POINT_cmp(x0, x1, x2, x3);
}

int _cffi_f_EC_POINT_copy(EC_POINT * x0, EC_POINT const * x1)
{
  return EC_POINT_copy(x0, x1);
}

int _cffi_f_EC_POINT_dbl(EC_GROUP const * x0, EC_POINT * x1, EC_POINT const * x2, BN_CTX * x3)
{
  return EC_POINT_dbl(x0, x1, x2, x3);
}

EC_POINT * _cffi_f_EC_POINT_dup(EC_POINT const * x0, EC_GROUP const * x1)
{
  return EC_POINT_dup(x0, x1);
}

void _cffi_f_EC_POINT_free(EC_POINT * x0)
{
  EC_POINT_free(x0);
}

int _cffi_f_EC_POINT_get_affine_coordinates_GFp(EC_GROUP const * x0, EC_POINT const * x1, BIGNUM * x2, BIGNUM * x3, BN_CTX * x4)
{
  return EC_POINT_get_affine_coordinates_GFp(x0, x1, x2, x3, x4);
}

int _cffi_f_EC_POINT_invert(EC_GROUP const * x0, EC_POINT * x1, BN_CTX * x2)
{
  return EC_POINT_invert(x0, x1, x2);
}

int _cffi_f_EC_POINT_is_at_infinity(EC_GROUP const * x0, EC_POINT const * x1)
{
  return EC_POINT_is_at_infinity(x0, x1);
}

int _cffi_f_EC_POINT_is_on_curve(EC_GROUP const * x0, EC_POINT const * x1, BN_CTX * x2)
{
  return EC_POINT_is_on_curve(x0, x1, x2);
}

int _cffi_f_EC_POINT_make_affine(EC_GROUP const * x0, EC_POINT * x1, BN_CTX * x2)
{
  return EC_POINT_make_affine(x0, x1, x2);
}

int _cffi_f_EC_POINT_mul(EC_GROUP const * x0, EC_POINT * x1, BIGNUM const * x2, EC_POINT const * x3, BIGNUM const * x4, BN_CTX * x5)
{
  return EC_POINT_mul(x0, x1, x2, x3, x4, x5);
}

EC_POINT * _cffi_f_EC_POINT_new(EC_GROUP const * x0)
{
  return EC_POINT_new(x0);
}

int _cffi_f_EC_POINT_oct2point(EC_GROUP const * x0, EC_POINT * x1, unsigned char const * x2, size_t x3, BN_CTX * x4)
{
  return EC_POINT_oct2point(x0, x1, x2, x3, x4);
}

size_t _cffi_f_EC_POINT_point2oct(EC_GROUP const * x0, EC_POINT const * x1, point_conversion_form_t x2, unsigned char * x3, size_t x4, BN_CTX * x5)
{
  return EC_POINT_point2oct(x0, x1, x2, x3, x4, x5);
}

int _cffi_f_EC_POINT_set_compressed_coordinates_GFp(EC_GROUP const * x0, EC_POINT * x1, BIGNUM const * x2, int x3, BN_CTX * x4)
{
  return EC_POINT_set_compressed_coordinates_GFp(x0, x1, x2, x3, x4);
}

int _cffi_f_EC_POINT_set_to_infinity(EC_GROUP const * x0, EC_POINT * x1)
{
  return EC_POINT_set_to_infinity(x0, x1);
}

int _cffi_f_EC_POINTs_make_affine(EC_GROUP const * x0, size_t x1, EC_POINT * * x2, BN_CTX * x3)
{
  return EC_POINTs_make_affine(x0, x1, x2, x3);
}

int _cffi_f_EC_POINTs_mul(EC_GROUP const * x0, EC_POINT * x1, BIGNUM const * x2, size_t x3, EC_POINT const * * x4, BIGNUM const * * x5, BN_CTX * x6)
{
  return EC_POINTs_mul(x0, x1, x2, x3, x4, x5, x6);
}

size_t _cffi_f_EC_get_builtin_curves(EC_builtin_curve * x0, size_t x1)
{
  return EC_get_builtin_curves(x0, x1);
}

int _cffi_f_EVP_CIPHER_CTX_cleanup(EVP_CIPHER_CTX * x0)
{
  return EVP_CIPHER_CTX_cleanup(x0);
}

int _cffi_f_EVP_CIPHER_CTX_ctrl(EVP_CIPHER_CTX * x0, int x1, int x2, void * x3)
{
  return EVP_CIPHER_CTX_ctrl(x0, x1, x2, x3);
}

void _cffi_f_EVP_CIPHER_CTX_free(EVP_CIPHER_CTX * x0)
{
  EVP_CIPHER_CTX_free(x0);
}

void _cffi_f_EVP_CIPHER_CTX_init(EVP_CIPHER_CTX * x0)
{
  EVP_CIPHER_CTX_init(x0);
}

EVP_CIPHER_CTX * _cffi_f_EVP_CIPHER_CTX_new(void)
{
  return EVP_CIPHER_CTX_new();
}

int _cffi_f_EVP_CIPHER_CTX_rand_key(EVP_CIPHER_CTX * x0, unsigned char * x1)
{
  return EVP_CIPHER_CTX_rand_key(x0, x1);
}

int _cffi_f_EVP_CIPHER_CTX_set_key_length(EVP_CIPHER_CTX * x0, int x1)
{
  return EVP_CIPHER_CTX_set_key_length(x0, x1);
}

int _cffi_f_EVP_CIPHER_CTX_set_padding(EVP_CIPHER_CTX * x0, int x1)
{
  return EVP_CIPHER_CTX_set_padding(x0, x1);
}

int _cffi_f_EVP_CipherFinal_ex(EVP_CIPHER_CTX * x0, unsigned char * x1, int * x2)
{
  return EVP_CipherFinal_ex(x0, x1, x2);
}

int _cffi_f_EVP_CipherInit_ex(EVP_CIPHER_CTX * x0, EVP_CIPHER const * x1, ENGINE * x2, unsigned char const * x3, unsigned char const * x4, int x5)
{
  return EVP_CipherInit_ex(x0, x1, x2, x3, x4, x5);
}

int _cffi_f_EVP_CipherUpdate(EVP_CIPHER_CTX * x0, unsigned char * x1, int * x2, unsigned char const * x3, int x4)
{
  return EVP_CipherUpdate(x0, x1, x2, x3, x4);
}

int _cffi_f_EVP_DecryptFinal_ex(EVP_CIPHER_CTX * x0, unsigned char * x1, int * x2)
{
  return EVP_DecryptFinal_ex(x0, x1, x2);
}

int _cffi_f_EVP_DecryptInit_ex(EVP_CIPHER_CTX * x0, EVP_CIPHER const * x1, ENGINE * x2, unsigned char * x3, unsigned char * x4)
{
  return EVP_DecryptInit_ex(x0, x1, x2, x3, x4);
}

int _cffi_f_EVP_DecryptUpdate(EVP_CIPHER_CTX * x0, unsigned char * x1, int * x2, unsigned char * x3, int x4)
{
  return EVP_DecryptUpdate(x0, x1, x2, x3, x4);
}

int _cffi_f_EVP_EncryptFinal_ex(EVP_CIPHER_CTX * x0, unsigned char * x1, int * x2)
{
  return EVP_EncryptFinal_ex(x0, x1, x2);
}

int _cffi_f_EVP_EncryptInit_ex(EVP_CIPHER_CTX * x0, EVP_CIPHER const * x1, ENGINE * x2, unsigned char * x3, unsigned char * x4)
{
  return EVP_EncryptInit_ex(x0, x1, x2, x3, x4);
}

int _cffi_f_EVP_EncryptUpdate(EVP_CIPHER_CTX * x0, unsigned char * x1, int * x2, unsigned char * x3, int x4)
{
  return EVP_EncryptUpdate(x0, x1, x2, x3, x4);
}

int _cffi_f_EVP_MD_block_size(EVP_MD const * x0)
{
  return EVP_MD_block_size(x0);
}

int _cffi_f_EVP_MD_size(EVP_MD const * x0)
{
  return EVP_MD_size(x0);
}

EVP_CIPHER const * _cffi_f_EVP_aes_128_gcm(void)
{
  return EVP_aes_128_gcm();
}

EVP_CIPHER const * _cffi_f_EVP_aes_192_gcm(void)
{
  return EVP_aes_192_gcm();
}

EVP_CIPHER const * _cffi_f_EVP_aes_256_gcm(void)
{
  return EVP_aes_256_gcm();
}

EVP_CIPHER const * _cffi_f_EVP_get_cipherbyname(char const * x0)
{
  return EVP_get_cipherbyname(x0);
}

EVP_MD const * _cffi_f_EVP_get_digestbyname(char const * x0)
{
  return EVP_get_digestbyname(x0);
}

void _cffi_f_HMAC_CTX_cleanup(HMAC_CTX * x0)
{
  HMAC_CTX_cleanup(x0);
}

void _cffi_f_HMAC_CTX_init(HMAC_CTX * x0)
{
  HMAC_CTX_init(x0);
}

int _cffi_f_HMAC_Final(HMAC_CTX * x0, unsigned char * x1, unsigned int * x2)
{
  return HMAC_Final(x0, x1, x2);
}

int _cffi_f_HMAC_Init_ex(HMAC_CTX * x0, void const * x1, int x2, EVP_MD const * x3, ENGINE * x4)
{
  return HMAC_Init_ex(x0, x1, x2, x3, x4);
}

int _cffi_f_HMAC_Update(HMAC_CTX * x0, unsigned char const * x1, int x2)
{
  return HMAC_Update(x0, x1, x2);
}

void _cffi_f_OPENSSL_free(void * x0)
{
  OPENSSL_free(x0);
}

char const * _cffi_f_SSLeay_version(int x0)
{
  return SSLeay_version(x0);
}

int _cffi_f_bn_is_odd(BIGNUM * x0)
{
  return bn_is_odd(x0);
}

int _cffi_f_bn_num_bytes(BIGNUM * x0)
{
  return bn_num_bytes(x0);
}

void _cffi_f_cleanup_ciphers(void)
{
  cleanup_ciphers();
}

size_t _cffi_f_hmac_ctx_size(void)
{
  return hmac_ctx_size();
}

void _cffi_f_init_ciphers(void)
{
  init_ciphers();
}

int _cffi_const_EVP_CTRL_AEAD_SET_MAC_KEY(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_AEAD_SET_MAC_KEY);
  return (EVP_CTRL_AEAD_SET_MAC_KEY) <= 0;
}

int _cffi_const_EVP_CTRL_AEAD_TLS1_AAD(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_AEAD_TLS1_AAD);
  return (EVP_CTRL_AEAD_TLS1_AAD) <= 0;
}

int _cffi_const_EVP_CTRL_CCM_GET_TAG(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_CCM_GET_TAG);
  return (EVP_CTRL_CCM_GET_TAG) <= 0;
}

int _cffi_const_EVP_CTRL_CCM_SET_IVLEN(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_CCM_SET_IVLEN);
  return (EVP_CTRL_CCM_SET_IVLEN) <= 0;
}

int _cffi_const_EVP_CTRL_CCM_SET_L(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_CCM_SET_L);
  return (EVP_CTRL_CCM_SET_L) <= 0;
}

int _cffi_const_EVP_CTRL_CCM_SET_MSGLEN(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_CCM_SET_MSGLEN);
  return (EVP_CTRL_CCM_SET_MSGLEN) <= 0;
}

int _cffi_const_EVP_CTRL_CCM_SET_TAG(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_CCM_SET_TAG);
  return (EVP_CTRL_CCM_SET_TAG) <= 0;
}

int _cffi_const_EVP_CTRL_COPY(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_COPY);
  return (EVP_CTRL_COPY) <= 0;
}

int _cffi_const_EVP_CTRL_GCM_GET_TAG(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GCM_GET_TAG);
  return (EVP_CTRL_GCM_GET_TAG) <= 0;
}

int _cffi_const_EVP_CTRL_GCM_IV_GEN(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GCM_IV_GEN);
  return (EVP_CTRL_GCM_IV_GEN) <= 0;
}

int _cffi_const_EVP_CTRL_GCM_SET_IVLEN(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GCM_SET_IVLEN);
  return (EVP_CTRL_GCM_SET_IVLEN) <= 0;
}

int _cffi_const_EVP_CTRL_GCM_SET_IV_FIXED(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GCM_SET_IV_FIXED);
  return (EVP_CTRL_GCM_SET_IV_FIXED) <= 0;
}

int _cffi_const_EVP_CTRL_GCM_SET_IV_INV(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GCM_SET_IV_INV);
  return (EVP_CTRL_GCM_SET_IV_INV) <= 0;
}

int _cffi_const_EVP_CTRL_GCM_SET_TAG(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GCM_SET_TAG);
  return (EVP_CTRL_GCM_SET_TAG) <= 0;
}

int _cffi_const_EVP_CTRL_GET_RC2_KEY_BITS(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GET_RC2_KEY_BITS);
  return (EVP_CTRL_GET_RC2_KEY_BITS) <= 0;
}

int _cffi_const_EVP_CTRL_GET_RC5_ROUNDS(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_GET_RC5_ROUNDS);
  return (EVP_CTRL_GET_RC5_ROUNDS) <= 0;
}

int _cffi_const_EVP_CTRL_INIT(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_INIT);
  return (EVP_CTRL_INIT) <= 0;
}

int _cffi_const_EVP_CTRL_PBE_PRF_NID(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_PBE_PRF_NID);
  return (EVP_CTRL_PBE_PRF_NID) <= 0;
}

int _cffi_const_EVP_CTRL_RAND_KEY(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_RAND_KEY);
  return (EVP_CTRL_RAND_KEY) <= 0;
}

int _cffi_const_EVP_CTRL_SET_KEY_LENGTH(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_SET_KEY_LENGTH);
  return (EVP_CTRL_SET_KEY_LENGTH) <= 0;
}

int _cffi_const_EVP_CTRL_SET_RC2_KEY_BITS(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_SET_RC2_KEY_BITS);
  return (EVP_CTRL_SET_RC2_KEY_BITS) <= 0;
}

int _cffi_const_EVP_CTRL_SET_RC5_ROUNDS(long long *out_value)
{
  *out_value = (long long)(EVP_CTRL_SET_RC5_ROUNDS);
  return (EVP_CTRL_SET_RC5_ROUNDS) <= 0;
}

int _cffi_const_SSLEAY_VERSION(long long *out_value)
{
  *out_value = (long long)(SSLEAY_VERSION);
  return (SSLEAY_VERSION) <= 0;
}

static void _cffi_check_struct_ECDSA_SIG_st(struct ECDSA_SIG_st *p)
{
  /* only to generate compile-time warnings or errors */
  { BIGNUM * *tmp = &p->r; (void)tmp; }
  { BIGNUM * *tmp = &p->s; (void)tmp; }
}
ssize_t _cffi_layout_struct_ECDSA_SIG_st(ssize_t i)
{
  struct _cffi_aligncheck { char x; struct ECDSA_SIG_st y; };
  static ssize_t nums[] = {
    sizeof(struct ECDSA_SIG_st),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct ECDSA_SIG_st, r),
    sizeof(((struct ECDSA_SIG_st *)0)->r),
    offsetof(struct ECDSA_SIG_st, s),
    sizeof(((struct ECDSA_SIG_st *)0)->s),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_ECDSA_SIG_st(0);
}

static void _cffi_check_struct_evp_cipher_ctx_st(struct evp_cipher_ctx_st *p)
{
  /* only to generate compile-time warnings or errors */
  { EVP_CIPHER const * *tmp = &p->cipher; (void)tmp; }
  (void)((p->encrypt) << 1);
  (void)((p->buf_len) << 1);
  (void)((p->num) << 1);
  (void)((p->key_len) << 1);
  (void)((p->flags) << 1);
  (void)((p->final_used) << 1);
  (void)((p->block_mask) << 1);
}
ssize_t _cffi_layout_struct_evp_cipher_ctx_st(ssize_t i)
{
  struct _cffi_aligncheck { char x; struct evp_cipher_ctx_st y; };
  static ssize_t nums[] = {
    sizeof(struct evp_cipher_ctx_st),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct evp_cipher_ctx_st, cipher),
    sizeof(((struct evp_cipher_ctx_st *)0)->cipher),
    offsetof(struct evp_cipher_ctx_st, encrypt),
    sizeof(((struct evp_cipher_ctx_st *)0)->encrypt),
    offsetof(struct evp_cipher_ctx_st, buf_len),
    sizeof(((struct evp_cipher_ctx_st *)0)->buf_len),
    offsetof(struct evp_cipher_ctx_st, num),
    sizeof(((struct evp_cipher_ctx_st *)0)->num),
    offsetof(struct evp_cipher_ctx_st, key_len),
    sizeof(((struct evp_cipher_ctx_st *)0)->key_len),
    offsetof(struct evp_cipher_ctx_st, flags),
    sizeof(((struct evp_cipher_ctx_st *)0)->flags),
    offsetof(struct evp_cipher_ctx_st, final_used),
    sizeof(((struct evp_cipher_ctx_st *)0)->final_used),
    offsetof(struct evp_cipher_ctx_st, block_mask),
    sizeof(((struct evp_cipher_ctx_st *)0)->block_mask),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_evp_cipher_ctx_st(0);
}

static void _cffi_check_struct_evp_cipher_st(struct evp_cipher_st *p)
{
  /* only to generate compile-time warnings or errors */
  (void)((p->nid) << 1);
  (void)((p->block_size) << 1);
  (void)((p->key_len) << 1);
  (void)((p->iv_len) << 1);
  (void)((p->flags) << 1);
}
ssize_t _cffi_layout_struct_evp_cipher_st(ssize_t i)
{
  struct _cffi_aligncheck { char x; struct evp_cipher_st y; };
  static ssize_t nums[] = {
    sizeof(struct evp_cipher_st),
    offsetof(struct _cffi_aligncheck, y),
    offsetof(struct evp_cipher_st, nid),
    sizeof(((struct evp_cipher_st *)0)->nid),
    offsetof(struct evp_cipher_st, block_size),
    sizeof(((struct evp_cipher_st *)0)->block_size),
    offsetof(struct evp_cipher_st, key_len),
    sizeof(((struct evp_cipher_st *)0)->key_len),
    offsetof(struct evp_cipher_st, iv_len),
    sizeof(((struct evp_cipher_st *)0)->iv_len),
    offsetof(struct evp_cipher_st, flags),
    sizeof(((struct evp_cipher_st *)0)->flags),
    -1
  };
  return nums[i];
  /* the next line is not executed, but compiled */
  _cffi_check_struct_evp_cipher_st(0);
}

