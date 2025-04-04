/* DO NOT EDIT THIS FILE - it is machine generated */
#include <jni.h>
/* Header for class com_flocto_notsus_NativeLib */

#ifndef _Included_com_flocto_notsus_NativeLib
#define _Included_com_flocto_notsus_NativeLib
#ifdef __cplusplus
extern "C" {
#endif
/*
 * Class:     com_flocto_notsus_NativeLib
 * Method:    getNativeString
 * Signature: ()Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_flocto_notsus_NativeLib_getNativeString
  (JNIEnv *, jobject);

/*
 * Class:     com_flocto_notsus_NativeLib
 * Method:    nativeBase64Encode
 * Signature: ([B)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_flocto_notsus_NativeLib_nativeBase64Encode
  (JNIEnv *, jobject, jbyteArray);

/*
 * Class:     com_flocto_notsus_NativeLib
 * Method:    nativeBase64Decode
 * Signature: ([B)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_flocto_notsus_NativeLib_nativeBase64Decode
  (JNIEnv *, jobject, jbyteArray);

/*
 * Class:     com_flocto_notsus_NativeLib
 * Method:    nativeEncryptData
 * Signature: ([B[B)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_flocto_notsus_NativeLib_nativeEncryptData
  (JNIEnv *, jobject, jbyteArray, jbyteArray);

/*
 * Class:     com_flocto_notsus_NativeLib
 * Method:    nativeDecryptData
 * Signature: ([B[B)Ljava/lang/String;
 */
JNIEXPORT jstring JNICALL Java_com_flocto_notsus_NativeLib_nativeDecryptData
  (JNIEnv *, jobject, jbyteArray, jbyteArray);

#ifdef __cplusplus
}
#endif
#endif
