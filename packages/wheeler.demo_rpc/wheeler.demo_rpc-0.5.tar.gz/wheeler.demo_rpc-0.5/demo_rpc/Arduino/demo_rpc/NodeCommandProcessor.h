#ifndef ___DEMO_RPC___
#define ___DEMO_RPC___

#include "Array.h"


#define BASE_NODE__NAME  ("demo_rpc")
#define BASE_NODE__MANUFACTURER  ("Wheeler Lab")
#define BASE_NODE__SOFTWARE_VERSION  ("0.5")
#define BASE_NODE__URL  ("http://github.com/wheeler-microfluidics/demo_rpc.git")


namespace demo_rpc {


struct MicrosecondsRequest {
};

struct MicrosecondsResponse {
  uint32_t result;
};

struct MillisecondsRequest {
};

struct MillisecondsResponse {
  uint32_t result;
};

struct DelayUsRequest {
  uint16_t us;
};

struct DelayUsResponse {
};

struct DelayMsRequest {
  uint16_t ms;
};

struct DelayMsResponse {
};

struct RamFreeRequest {
};

struct RamFreeResponse {
  uint32_t result;
};

struct PinModeRequest {
  uint8_t pin;
  uint8_t mode;
};

struct PinModeResponse {
};

struct DigitalReadRequest {
  uint8_t pin;
};

struct DigitalReadResponse {
  uint8_t result;
};

struct DigitalWriteRequest {
  uint8_t pin;
  uint8_t value;
};

struct DigitalWriteResponse {
};

struct AnalogReadRequest {
  uint8_t pin;
};

struct AnalogReadResponse {
  uint16_t result;
};

struct AnalogWriteRequest {
  uint8_t pin;
  uint8_t value;
};

struct AnalogWriteResponse {
};

struct ArrayLengthRequest {
  UInt8Array array;
};

struct ArrayLengthResponse {
  uint16_t result;
};

struct EchoArrayRequest {
  UInt32Array array;
};

struct EchoArrayResponse {
  UInt32Array result;
};

struct StrEchoRequest {
  UInt8Array msg;
};

struct StrEchoResponse {
  UInt8Array result;
};

struct BaseNodeSoftwareVersionRequest {
};

struct BaseNodeSoftwareVersionResponse {
  UInt8Array result;
};

struct NameRequest {
};

struct NameResponse {
  UInt8Array result;
};

struct ManufacturerRequest {
};

struct ManufacturerResponse {
  UInt8Array result;
};

struct SoftwareVersionRequest {
};

struct SoftwareVersionResponse {
  UInt8Array result;
};

struct UrlRequest {
};

struct UrlResponse {
  UInt8Array result;
};

struct UpdateEepromBlockRequest {
  uint16_t address;
  UInt8Array data;
};

struct UpdateEepromBlockResponse {
};

struct ReadEepromBlockRequest {
  uint16_t address;
  uint16_t n;
};

struct ReadEepromBlockResponse {
  UInt8Array result;
};

struct I2cAddressRequest {
};

struct I2cAddressResponse {
  uint8_t result;
};

struct I2cBufferSizeRequest {
};

struct I2cBufferSizeResponse {
  uint16_t result;
};

struct I2cScanRequest {
};

struct I2cScanResponse {
  UInt8Array result;
};

struct I2cAvailableRequest {
};

struct I2cAvailableResponse {
  int16_t result;
};

struct I2cReadByteRequest {
};

struct I2cReadByteResponse {
  int8_t result;
};

struct I2cRequestFromRequest {
  uint8_t address;
  uint8_t n_bytes_to_read;
};

struct I2cRequestFromResponse {
  int8_t result;
};

struct I2cReadRequest {
  uint8_t address;
  uint8_t n_bytes_to_read;
};

struct I2cReadResponse {
  UInt8Array result;
};

struct I2cWriteRequest {
  uint8_t address;
  UInt8Array data;
};

struct I2cWriteResponse {
};

struct I2cRequestRequest {
  uint8_t address;
  UInt8Array data;
};

struct I2cRequestResponse {
  UInt8Array result;
};

struct LoadConfigRequest {
};

struct LoadConfigResponse {
};

struct SaveConfigRequest {
};

struct SaveConfigResponse {
};

struct ResetConfigRequest {
};

struct ResetConfigResponse {
};

struct SerializeConfigRequest {
};

struct SerializeConfigResponse {
  UInt8Array result;
};

struct UpdateConfigRequest {
  UInt8Array serialized;
};

struct UpdateConfigResponse {
  uint8_t result;
};

struct ResetStateRequest {
};

struct ResetStateResponse {
};

struct SerializeStateRequest {
};

struct SerializeStateResponse {
  UInt8Array result;
};

struct UpdateStateRequest {
  UInt8Array serialized;
};

struct UpdateStateResponse {
  uint8_t result;
};

struct GetBufferRequest {
};

struct GetBufferResponse {
  UInt8Array result;
};

struct BeginRequest {
};

struct BeginResponse {
};

struct PacketCrcRequest {
  UInt8Array data;
};

struct PacketCrcResponse {
  uint16_t result;
};

struct TestParserRequest {
  UInt8Array data;
};

struct TestParserResponse {
  UInt8Array result;
};

struct SetI2cAddressRequest {
  uint8_t value;
};

struct SetI2cAddressResponse {
};

struct SetSerialNumberRequest {
  uint32_t value;
};

struct SetSerialNumberResponse {
};

struct SerialNumberRequest {
};

struct SerialNumberResponse {
  uint32_t result;
};

struct MaxPayloadSizeRequest {
};

struct MaxPayloadSizeResponse {
  uint32_t result;
};

struct SizeofNodeRequest {
};

struct SizeofNodeResponse {
  uint32_t result;
};

struct SizeofConfigRequest {
};

struct SizeofConfigResponse {
  uint32_t result;
};

struct SizeofStateRequest {
};

struct SizeofStateResponse {
  uint32_t result;
};

struct SizeofParserRequest {
};

struct SizeofParserResponse {
  uint32_t result;
};

struct SizeofPacketStructRequest {
};

struct SizeofPacketStructResponse {
  uint32_t result;
};

struct SizeofPacketRequest {
};

struct SizeofPacketResponse {
  uint32_t result;
};

struct SizeofSerialHandlerRequest {
};

struct SizeofSerialHandlerResponse {
  uint32_t result;
};

struct SizeofI2cHandlerRequest {
};

struct SizeofI2cHandlerResponse {
  uint32_t result;
};


template <typename Obj>
class CommandProcessor {
  /* # `CommandProcessor` #
   *
   * Each call to this functor processes a single command.
   *
   * All arguments are passed by reference, such that they may be used to form
   * a response.  If the integer return value of the call is zero, the call is
   * assumed to have no response required.  Otherwise, the arguments contain
   * must contain response values. */
protected:
  Obj &obj_;
public:
  CommandProcessor(Obj &obj) : obj_(obj) {}


    static const int CMD_MICROSECONDS = 0x00;
    static const int CMD_MILLISECONDS = 0x01;
    static const int CMD_DELAY_US = 0x02;
    static const int CMD_DELAY_MS = 0x03;
    static const int CMD_RAM_FREE = 0x05;
    static const int CMD_PIN_MODE = 0x06;
    static const int CMD_DIGITAL_READ = 0x07;
    static const int CMD_DIGITAL_WRITE = 0x08;
    static const int CMD_ANALOG_READ = 0x09;
    static const int CMD_ANALOG_WRITE = 0x0a;
    static const int CMD_ARRAY_LENGTH = 0x0b;
    static const int CMD_ECHO_ARRAY = 0x0c;
    static const int CMD_STR_ECHO = 0x0d;
    static const int CMD_BASE_NODE_SOFTWARE_VERSION = 0x0e;
    static const int CMD_NAME = 0x0f;
    static const int CMD_MANUFACTURER = 0x10;
    static const int CMD_SOFTWARE_VERSION = 0x11;
    static const int CMD_URL = 0x12;
    static const int CMD_UPDATE_EEPROM_BLOCK = 0x20;
    static const int CMD_READ_EEPROM_BLOCK = 0x21;
    static const int CMD_I2C_ADDRESS = 0x41;
    static const int CMD_I2C_BUFFER_SIZE = 0x42;
    static const int CMD_I2C_SCAN = 0x43;
    static const int CMD_I2C_AVAILABLE = 0x44;
    static const int CMD_I2C_READ_BYTE = 0x45;
    static const int CMD_I2C_REQUEST_FROM = 0x46;
    static const int CMD_I2C_READ = 0x47;
    static const int CMD_I2C_WRITE = 0x48;
    static const int CMD_I2C_REQUEST = 0x60;
    static const int CMD_LOAD_CONFIG = 0x80;
    static const int CMD_SAVE_CONFIG = 0x81;
    static const int CMD_RESET_CONFIG = 0x82;
    static const int CMD_SERIALIZE_CONFIG = 0x83;
    static const int CMD_UPDATE_CONFIG = 0x84;
    static const int CMD_RESET_STATE = 0xa0;
    static const int CMD_SERIALIZE_STATE = 0xa1;
    static const int CMD_UPDATE_STATE = 0xa2;
    static const int CMD_GET_BUFFER = 0xc0;
    static const int CMD_BEGIN = 0xc1;
    static const int CMD_PACKET_CRC = 0xc2;
    static const int CMD_TEST_PARSER = 0xc3;
    static const int CMD_SET_I2C_ADDRESS = 0xc4;
    static const int CMD_SET_SERIAL_NUMBER = 0xc5;
    static const int CMD_SERIAL_NUMBER = 0xc6;
    static const int CMD_MAX_PAYLOAD_SIZE = 0xc7;
    static const int CMD_SIZEOF_NODE = 0xc8;
    static const int CMD_SIZEOF_CONFIG = 0xc9;
    static const int CMD_SIZEOF_STATE = 0xca;
    static const int CMD_SIZEOF_PARSER = 0xcb;
    static const int CMD_SIZEOF_PACKET_STRUCT = 0xcc;
    static const int CMD_SIZEOF_PACKET = 0xcd;
    static const int CMD_SIZEOF_SERIAL_HANDLER = 0xce;
    static const int CMD_SIZEOF_I2C_HANDLER = 0xcf;

  UInt8Array process_command(UInt8Array request_arr, UInt8Array buffer) {
    /* ## Call operator ##
     *
     * Arguments:
     *
     *  - `request_arr`: Serialized command request structure array,
     *  - `buffer`: Buffer array (available for writing output). */

    UInt8Array result;

    // Interpret first byte of request as command code.
    switch (request_arr.data[0]) {

        case CMD_MICROSECONDS:
          {
            /* Cast buffer as request. */
            MicrosecondsRequest &request = *(reinterpret_cast
                                          <MicrosecondsRequest *>
                                          (&request_arr.data[1]));
    
            MicrosecondsResponse response;

            response.result =
            obj_.microseconds();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            MicrosecondsResponse &output = *(reinterpret_cast
                                                 <MicrosecondsResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_MILLISECONDS:
          {
            /* Cast buffer as request. */
            MillisecondsRequest &request = *(reinterpret_cast
                                          <MillisecondsRequest *>
                                          (&request_arr.data[1]));
    
            MillisecondsResponse response;

            response.result =
            obj_.milliseconds();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            MillisecondsResponse &output = *(reinterpret_cast
                                                 <MillisecondsResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_DELAY_US:
          {
            /* Cast buffer as request. */
            DelayUsRequest &request = *(reinterpret_cast
                                          <DelayUsRequest *>
                                          (&request_arr.data[1]));
    
            obj_.delay_us(request.us);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_DELAY_MS:
          {
            /* Cast buffer as request. */
            DelayMsRequest &request = *(reinterpret_cast
                                          <DelayMsRequest *>
                                          (&request_arr.data[1]));
    
            obj_.delay_ms(request.ms);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_RAM_FREE:
          {
            /* Cast buffer as request. */
            RamFreeRequest &request = *(reinterpret_cast
                                          <RamFreeRequest *>
                                          (&request_arr.data[1]));
    
            RamFreeResponse response;

            response.result =
            obj_.ram_free();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            RamFreeResponse &output = *(reinterpret_cast
                                                 <RamFreeResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_PIN_MODE:
          {
            /* Cast buffer as request. */
            PinModeRequest &request = *(reinterpret_cast
                                          <PinModeRequest *>
                                          (&request_arr.data[1]));
    
            obj_.pin_mode(request.pin, request.mode);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_DIGITAL_READ:
          {
            /* Cast buffer as request. */
            DigitalReadRequest &request = *(reinterpret_cast
                                          <DigitalReadRequest *>
                                          (&request_arr.data[1]));
    
            DigitalReadResponse response;

            response.result =
            obj_.digital_read(request.pin);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            DigitalReadResponse &output = *(reinterpret_cast
                                                 <DigitalReadResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_DIGITAL_WRITE:
          {
            /* Cast buffer as request. */
            DigitalWriteRequest &request = *(reinterpret_cast
                                          <DigitalWriteRequest *>
                                          (&request_arr.data[1]));
    
            obj_.digital_write(request.pin, request.value);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_ANALOG_READ:
          {
            /* Cast buffer as request. */
            AnalogReadRequest &request = *(reinterpret_cast
                                          <AnalogReadRequest *>
                                          (&request_arr.data[1]));
    
            AnalogReadResponse response;

            response.result =
            obj_.analog_read(request.pin);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            AnalogReadResponse &output = *(reinterpret_cast
                                                 <AnalogReadResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_ANALOG_WRITE:
          {
            /* Cast buffer as request. */
            AnalogWriteRequest &request = *(reinterpret_cast
                                          <AnalogWriteRequest *>
                                          (&request_arr.data[1]));
    
            obj_.analog_write(request.pin, request.value);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_ARRAY_LENGTH:
          {
            /* Cast buffer as request. */
            ArrayLengthRequest &request = *(reinterpret_cast
                                          <ArrayLengthRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.array.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.array.data);
            ArrayLengthResponse response;

            response.result =
            obj_.array_length(request.array);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            ArrayLengthResponse &output = *(reinterpret_cast
                                                 <ArrayLengthResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_ECHO_ARRAY:
          {
            /* Cast buffer as request. */
            EchoArrayRequest &request = *(reinterpret_cast
                                          <EchoArrayRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.array.data = (uint32_t *)((uint8_t *)&request + (uint16_t)request.array.data);
            EchoArrayResponse response;

            response.result =
            obj_.echo_array(request.array);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_STR_ECHO:
          {
            /* Cast buffer as request. */
            StrEchoRequest &request = *(reinterpret_cast
                                          <StrEchoRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.msg.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.msg.data);
            StrEchoResponse response;

            response.result =
            obj_.str_echo(request.msg);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_BASE_NODE_SOFTWARE_VERSION:
          {
            /* Cast buffer as request. */
            BaseNodeSoftwareVersionRequest &request = *(reinterpret_cast
                                          <BaseNodeSoftwareVersionRequest *>
                                          (&request_arr.data[1]));
    
            BaseNodeSoftwareVersionResponse response;

            response.result =
            obj_.base_node_software_version();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_NAME:
          {
            /* Cast buffer as request. */
            NameRequest &request = *(reinterpret_cast
                                          <NameRequest *>
                                          (&request_arr.data[1]));
    
            NameResponse response;

            response.result =
            obj_.name();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_MANUFACTURER:
          {
            /* Cast buffer as request. */
            ManufacturerRequest &request = *(reinterpret_cast
                                          <ManufacturerRequest *>
                                          (&request_arr.data[1]));
    
            ManufacturerResponse response;

            response.result =
            obj_.manufacturer();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_SOFTWARE_VERSION:
          {
            /* Cast buffer as request. */
            SoftwareVersionRequest &request = *(reinterpret_cast
                                          <SoftwareVersionRequest *>
                                          (&request_arr.data[1]));
    
            SoftwareVersionResponse response;

            response.result =
            obj_.software_version();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_URL:
          {
            /* Cast buffer as request. */
            UrlRequest &request = *(reinterpret_cast
                                          <UrlRequest *>
                                          (&request_arr.data[1]));
    
            UrlResponse response;

            response.result =
            obj_.url();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_UPDATE_EEPROM_BLOCK:
          {
            /* Cast buffer as request. */
            UpdateEepromBlockRequest &request = *(reinterpret_cast
                                          <UpdateEepromBlockRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.data.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.data.data);
            obj_.update_eeprom_block(request.address, request.data);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_READ_EEPROM_BLOCK:
          {
            /* Cast buffer as request. */
            ReadEepromBlockRequest &request = *(reinterpret_cast
                                          <ReadEepromBlockRequest *>
                                          (&request_arr.data[1]));
    
            ReadEepromBlockResponse response;

            response.result =
            obj_.read_eeprom_block(request.address, request.n);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_I2C_ADDRESS:
          {
            /* Cast buffer as request. */
            I2cAddressRequest &request = *(reinterpret_cast
                                          <I2cAddressRequest *>
                                          (&request_arr.data[1]));
    
            I2cAddressResponse response;

            response.result =
            obj_.i2c_address();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cAddressResponse &output = *(reinterpret_cast
                                                 <I2cAddressResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_BUFFER_SIZE:
          {
            /* Cast buffer as request. */
            I2cBufferSizeRequest &request = *(reinterpret_cast
                                          <I2cBufferSizeRequest *>
                                          (&request_arr.data[1]));
    
            I2cBufferSizeResponse response;

            response.result =
            obj_.i2c_buffer_size();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cBufferSizeResponse &output = *(reinterpret_cast
                                                 <I2cBufferSizeResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_SCAN:
          {
            /* Cast buffer as request. */
            I2cScanRequest &request = *(reinterpret_cast
                                          <I2cScanRequest *>
                                          (&request_arr.data[1]));
    
            I2cScanResponse response;

            response.result =
            obj_.i2c_scan();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_I2C_AVAILABLE:
          {
            /* Cast buffer as request. */
            I2cAvailableRequest &request = *(reinterpret_cast
                                          <I2cAvailableRequest *>
                                          (&request_arr.data[1]));
    
            I2cAvailableResponse response;

            response.result =
            obj_.i2c_available();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cAvailableResponse &output = *(reinterpret_cast
                                                 <I2cAvailableResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_READ_BYTE:
          {
            /* Cast buffer as request. */
            I2cReadByteRequest &request = *(reinterpret_cast
                                          <I2cReadByteRequest *>
                                          (&request_arr.data[1]));
    
            I2cReadByteResponse response;

            response.result =
            obj_.i2c_read_byte();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cReadByteResponse &output = *(reinterpret_cast
                                                 <I2cReadByteResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_REQUEST_FROM:
          {
            /* Cast buffer as request. */
            I2cRequestFromRequest &request = *(reinterpret_cast
                                          <I2cRequestFromRequest *>
                                          (&request_arr.data[1]));
    
            I2cRequestFromResponse response;

            response.result =
            obj_.i2c_request_from(request.address, request.n_bytes_to_read);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cRequestFromResponse &output = *(reinterpret_cast
                                                 <I2cRequestFromResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_READ:
          {
            /* Cast buffer as request. */
            I2cReadRequest &request = *(reinterpret_cast
                                          <I2cReadRequest *>
                                          (&request_arr.data[1]));
    
            I2cReadResponse response;

            response.result =
            obj_.i2c_read(request.address, request.n_bytes_to_read);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_I2C_WRITE:
          {
            /* Cast buffer as request. */
            I2cWriteRequest &request = *(reinterpret_cast
                                          <I2cWriteRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.data.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.data.data);
            obj_.i2c_write(request.address, request.data);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_I2C_REQUEST:
          {
            /* Cast buffer as request. */
            I2cRequestRequest &request = *(reinterpret_cast
                                          <I2cRequestRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.data.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.data.data);
            I2cRequestResponse response;

            response.result =
            obj_.i2c_request(request.address, request.data);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_LOAD_CONFIG:
          {
            /* Cast buffer as request. */
            LoadConfigRequest &request = *(reinterpret_cast
                                          <LoadConfigRequest *>
                                          (&request_arr.data[1]));
    
            obj_.load_config();
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_SAVE_CONFIG:
          {
            /* Cast buffer as request. */
            SaveConfigRequest &request = *(reinterpret_cast
                                          <SaveConfigRequest *>
                                          (&request_arr.data[1]));
    
            obj_.save_config();
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_RESET_CONFIG:
          {
            /* Cast buffer as request. */
            ResetConfigRequest &request = *(reinterpret_cast
                                          <ResetConfigRequest *>
                                          (&request_arr.data[1]));
    
            obj_.reset_config();
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_SERIALIZE_CONFIG:
          {
            /* Cast buffer as request. */
            SerializeConfigRequest &request = *(reinterpret_cast
                                          <SerializeConfigRequest *>
                                          (&request_arr.data[1]));
    
            SerializeConfigResponse response;

            response.result =
            obj_.serialize_config();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_UPDATE_CONFIG:
          {
            /* Cast buffer as request. */
            UpdateConfigRequest &request = *(reinterpret_cast
                                          <UpdateConfigRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.serialized.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.serialized.data);
            UpdateConfigResponse response;

            response.result =
            obj_.update_config(request.serialized);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            UpdateConfigResponse &output = *(reinterpret_cast
                                                 <UpdateConfigResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_RESET_STATE:
          {
            /* Cast buffer as request. */
            ResetStateRequest &request = *(reinterpret_cast
                                          <ResetStateRequest *>
                                          (&request_arr.data[1]));
    
            obj_.reset_state();
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_SERIALIZE_STATE:
          {
            /* Cast buffer as request. */
            SerializeStateRequest &request = *(reinterpret_cast
                                          <SerializeStateRequest *>
                                          (&request_arr.data[1]));
    
            SerializeStateResponse response;

            response.result =
            obj_.serialize_state();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_UPDATE_STATE:
          {
            /* Cast buffer as request. */
            UpdateStateRequest &request = *(reinterpret_cast
                                          <UpdateStateRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.serialized.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.serialized.data);
            UpdateStateResponse response;

            response.result =
            obj_.update_state(request.serialized);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            UpdateStateResponse &output = *(reinterpret_cast
                                                 <UpdateStateResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_GET_BUFFER:
          {
            /* Cast buffer as request. */
            GetBufferRequest &request = *(reinterpret_cast
                                          <GetBufferRequest *>
                                          (&request_arr.data[1]));
    
            GetBufferResponse response;

            response.result =
            obj_.get_buffer();
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_BEGIN:
          {
            /* Cast buffer as request. */
            BeginRequest &request = *(reinterpret_cast
                                          <BeginRequest *>
                                          (&request_arr.data[1]));
    
            obj_.begin();
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_PACKET_CRC:
          {
            /* Cast buffer as request. */
            PacketCrcRequest &request = *(reinterpret_cast
                                          <PacketCrcRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.data.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.data.data);
            PacketCrcResponse response;

            response.result =
            obj_.packet_crc(request.data);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            PacketCrcResponse &output = *(reinterpret_cast
                                                 <PacketCrcResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_TEST_PARSER:
          {
            /* Cast buffer as request. */
            TestParserRequest &request = *(reinterpret_cast
                                          <TestParserRequest *>
                                          (&request_arr.data[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.data.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.data.data);
            TestParserResponse response;

            response.result =
            obj_.test_parser(request.data);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_SET_I2C_ADDRESS:
          {
            /* Cast buffer as request. */
            SetI2cAddressRequest &request = *(reinterpret_cast
                                          <SetI2cAddressRequest *>
                                          (&request_arr.data[1]));
    
            obj_.set_i2c_address(request.value);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_SET_SERIAL_NUMBER:
          {
            /* Cast buffer as request. */
            SetSerialNumberRequest &request = *(reinterpret_cast
                                          <SetSerialNumberRequest *>
                                          (&request_arr.data[1]));
    
            obj_.set_serial_number(request.value);
    
        result.data = buffer.data;
        result.length = 0;
          }
          break;

        case CMD_SERIAL_NUMBER:
          {
            /* Cast buffer as request. */
            SerialNumberRequest &request = *(reinterpret_cast
                                          <SerialNumberRequest *>
                                          (&request_arr.data[1]));
    
            SerialNumberResponse response;

            response.result =
            obj_.serial_number();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SerialNumberResponse &output = *(reinterpret_cast
                                                 <SerialNumberResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_MAX_PAYLOAD_SIZE:
          {
            /* Cast buffer as request. */
            MaxPayloadSizeRequest &request = *(reinterpret_cast
                                          <MaxPayloadSizeRequest *>
                                          (&request_arr.data[1]));
    
            MaxPayloadSizeResponse response;

            response.result =
            obj_.max_payload_size();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            MaxPayloadSizeResponse &output = *(reinterpret_cast
                                                 <MaxPayloadSizeResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_NODE:
          {
            /* Cast buffer as request. */
            SizeofNodeRequest &request = *(reinterpret_cast
                                          <SizeofNodeRequest *>
                                          (&request_arr.data[1]));
    
            SizeofNodeResponse response;

            response.result =
            obj_.sizeof_node();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofNodeResponse &output = *(reinterpret_cast
                                                 <SizeofNodeResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_CONFIG:
          {
            /* Cast buffer as request. */
            SizeofConfigRequest &request = *(reinterpret_cast
                                          <SizeofConfigRequest *>
                                          (&request_arr.data[1]));
    
            SizeofConfigResponse response;

            response.result =
            obj_.sizeof_config();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofConfigResponse &output = *(reinterpret_cast
                                                 <SizeofConfigResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_STATE:
          {
            /* Cast buffer as request. */
            SizeofStateRequest &request = *(reinterpret_cast
                                          <SizeofStateRequest *>
                                          (&request_arr.data[1]));
    
            SizeofStateResponse response;

            response.result =
            obj_.sizeof_state();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofStateResponse &output = *(reinterpret_cast
                                                 <SizeofStateResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_PARSER:
          {
            /* Cast buffer as request. */
            SizeofParserRequest &request = *(reinterpret_cast
                                          <SizeofParserRequest *>
                                          (&request_arr.data[1]));
    
            SizeofParserResponse response;

            response.result =
            obj_.sizeof_parser();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofParserResponse &output = *(reinterpret_cast
                                                 <SizeofParserResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_PACKET_STRUCT:
          {
            /* Cast buffer as request. */
            SizeofPacketStructRequest &request = *(reinterpret_cast
                                          <SizeofPacketStructRequest *>
                                          (&request_arr.data[1]));
    
            SizeofPacketStructResponse response;

            response.result =
            obj_.sizeof_packet_struct();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofPacketStructResponse &output = *(reinterpret_cast
                                                 <SizeofPacketStructResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_PACKET:
          {
            /* Cast buffer as request. */
            SizeofPacketRequest &request = *(reinterpret_cast
                                          <SizeofPacketRequest *>
                                          (&request_arr.data[1]));
    
            SizeofPacketResponse response;

            response.result =
            obj_.sizeof_packet();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofPacketResponse &output = *(reinterpret_cast
                                                 <SizeofPacketResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_SERIAL_HANDLER:
          {
            /* Cast buffer as request. */
            SizeofSerialHandlerRequest &request = *(reinterpret_cast
                                          <SizeofSerialHandlerRequest *>
                                          (&request_arr.data[1]));
    
            SizeofSerialHandlerResponse response;

            response.result =
            obj_.sizeof_serial_handler();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofSerialHandlerResponse &output = *(reinterpret_cast
                                                 <SizeofSerialHandlerResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

        case CMD_SIZEOF_I2C_HANDLER:
          {
            /* Cast buffer as request. */
            SizeofI2cHandlerRequest &request = *(reinterpret_cast
                                          <SizeofI2cHandlerRequest *>
                                          (&request_arr.data[1]));
    
            SizeofI2cHandlerResponse response;

            response.result =
            obj_.sizeof_i2c_handler();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SizeofI2cHandlerResponse &output = *(reinterpret_cast
                                                 <SizeofI2cHandlerResponse *>
                                                 (&buffer.data[0]));
            output = response;
            result.data = buffer.data;
            result.length = sizeof(output);
          }
          break;

      default:
        result.length = 0xFFFF;
        result.data = NULL;
    }
    return result;
  }
};

}  // namespace demo_rpc



#endif  // ifndef ___DEMO_RPC___
