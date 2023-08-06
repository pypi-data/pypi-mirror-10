#ifndef ___DEMO_RPC___
#define ___DEMO_RPC___

#include "Array.h"
#include "remote_i2c_command.h"

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

struct MaxPayloadSizeRequest {
};

struct MaxPayloadSizeResponse {
  uint32_t result;
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

struct I2cAddressRequest {
};

struct I2cAddressResponse {
  int32_t result;
};

struct SetI2cAddressRequest {
  uint8_t address;
};

struct SetI2cAddressResponse {
  int32_t result;
};

struct TestMethodRequest {
};

struct TestMethodResponse {
  int32_t result;
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
    static const int CMD_MAX_PAYLOAD_SIZE = 0x04;
    static const int CMD_RAM_FREE = 0x05;
    static const int CMD_PIN_MODE = 0x06;
    static const int CMD_DIGITAL_READ = 0x07;
    static const int CMD_DIGITAL_WRITE = 0x08;
    static const int CMD_ANALOG_READ = 0x09;
    static const int CMD_ANALOG_WRITE = 0x0a;
    static const int CMD_ARRAY_LENGTH = 0x0b;
    static const int CMD_ECHO_ARRAY = 0x0c;
    static const int CMD_STR_ECHO = 0x0d;
    static const int CMD_I2C_ADDRESS = 0x0e;
    static const int CMD_SET_I2C_ADDRESS = 0x0f;
    static const int CMD_TEST_METHOD = 0x30;

  int process_command(uint16_t request_size, uint16_t buffer_size,
                      uint8_t *buffer) {
    /* ## Call operator ##
     *
     * Arguments:
     *
     *  - `request`: Protocol buffer command request structure,
     *  - `buffer_size`: The number of bytes in the arguments buffer.
     *  - `data`: The arguments buffer. */
    uint8_t command = buffer[0];
    int bytes_read = 0;
    int bytes_written = 0;

    /* Set the sub-request fields type based on the decoded message identifier
     * tag, which corresponds to a value in the `CommandType` enumerated type.
     */
    switch (command) {

        case CMD_MICROSECONDS:
          {
            /* Cast buffer as request. */
            MicrosecondsRequest &request = *(reinterpret_cast
                                          <MicrosecondsRequest *>
                                          (&buffer[1]));
    
            MicrosecondsResponse response;

            response.result =
            obj_.microseconds();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            MicrosecondsResponse &output = *(reinterpret_cast
                                                 <MicrosecondsResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_MILLISECONDS:
          {
            /* Cast buffer as request. */
            MillisecondsRequest &request = *(reinterpret_cast
                                          <MillisecondsRequest *>
                                          (&buffer[1]));
    
            MillisecondsResponse response;

            response.result =
            obj_.milliseconds();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            MillisecondsResponse &output = *(reinterpret_cast
                                                 <MillisecondsResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_DELAY_US:
          {
            /* Cast buffer as request. */
            DelayUsRequest &request = *(reinterpret_cast
                                          <DelayUsRequest *>
                                          (&buffer[1]));
    
            obj_.delay_us(request.us);
    
          }
          break;

        case CMD_DELAY_MS:
          {
            /* Cast buffer as request. */
            DelayMsRequest &request = *(reinterpret_cast
                                          <DelayMsRequest *>
                                          (&buffer[1]));
    
            obj_.delay_ms(request.ms);
    
          }
          break;

        case CMD_MAX_PAYLOAD_SIZE:
          {
            /* Cast buffer as request. */
            MaxPayloadSizeRequest &request = *(reinterpret_cast
                                          <MaxPayloadSizeRequest *>
                                          (&buffer[1]));
    
            MaxPayloadSizeResponse response;

            response.result =
            obj_.max_payload_size();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            MaxPayloadSizeResponse &output = *(reinterpret_cast
                                                 <MaxPayloadSizeResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_RAM_FREE:
          {
            /* Cast buffer as request. */
            RamFreeRequest &request = *(reinterpret_cast
                                          <RamFreeRequest *>
                                          (&buffer[1]));
    
            RamFreeResponse response;

            response.result =
            obj_.ram_free();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            RamFreeResponse &output = *(reinterpret_cast
                                                 <RamFreeResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_PIN_MODE:
          {
            /* Cast buffer as request. */
            PinModeRequest &request = *(reinterpret_cast
                                          <PinModeRequest *>
                                          (&buffer[1]));
    
            obj_.pin_mode(request.pin, request.mode);
    
          }
          break;

        case CMD_DIGITAL_READ:
          {
            /* Cast buffer as request. */
            DigitalReadRequest &request = *(reinterpret_cast
                                          <DigitalReadRequest *>
                                          (&buffer[1]));
    
            DigitalReadResponse response;

            response.result =
            obj_.digital_read(request.pin);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            DigitalReadResponse &output = *(reinterpret_cast
                                                 <DigitalReadResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_DIGITAL_WRITE:
          {
            /* Cast buffer as request. */
            DigitalWriteRequest &request = *(reinterpret_cast
                                          <DigitalWriteRequest *>
                                          (&buffer[1]));
    
            obj_.digital_write(request.pin, request.value);
    
          }
          break;

        case CMD_ANALOG_READ:
          {
            /* Cast buffer as request. */
            AnalogReadRequest &request = *(reinterpret_cast
                                          <AnalogReadRequest *>
                                          (&buffer[1]));
    
            AnalogReadResponse response;

            response.result =
            obj_.analog_read(request.pin);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            AnalogReadResponse &output = *(reinterpret_cast
                                                 <AnalogReadResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_ANALOG_WRITE:
          {
            /* Cast buffer as request. */
            AnalogWriteRequest &request = *(reinterpret_cast
                                          <AnalogWriteRequest *>
                                          (&buffer[1]));
    
            obj_.analog_write(request.pin, request.value);
    
          }
          break;

        case CMD_ARRAY_LENGTH:
          {
            /* Cast buffer as request. */
            ArrayLengthRequest &request = *(reinterpret_cast
                                          <ArrayLengthRequest *>
                                          (&buffer[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.array.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.array.data);
            ArrayLengthResponse response;

            response.result =
            obj_.array_length(request.array);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            ArrayLengthResponse &output = *(reinterpret_cast
                                                 <ArrayLengthResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_ECHO_ARRAY:
          {
            /* Cast buffer as request. */
            EchoArrayRequest &request = *(reinterpret_cast
                                          <EchoArrayRequest *>
                                          (&buffer[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.array.data = (uint32_t *)((uint8_t *)&request + (uint16_t)request.array.data);
            EchoArrayResponse response;

            response.result =
            obj_.echo_array(request.array);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            memcpy(&buffer[0], (uint8_t *)response.result.data, length);
            bytes_written += length;
          }
          break;

        case CMD_STR_ECHO:
          {
            /* Cast buffer as request. */
            StrEchoRequest &request = *(reinterpret_cast
                                          <StrEchoRequest *>
                                          (&buffer[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.msg.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.msg.data);
            StrEchoResponse response;

            response.result =
            obj_.str_echo(request.msg);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            memcpy(&buffer[0], (uint8_t *)response.result.data, length);
            bytes_written += length;
          }
          break;

        case CMD_I2C_ADDRESS:
          {
            /* Cast buffer as request. */
            I2cAddressRequest &request = *(reinterpret_cast
                                          <I2cAddressRequest *>
                                          (&buffer[1]));
    
            I2cAddressResponse response;

            response.result =
            obj_.i2c_address();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cAddressResponse &output = *(reinterpret_cast
                                                 <I2cAddressResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_SET_I2C_ADDRESS:
          {
            /* Cast buffer as request. */
            SetI2cAddressRequest &request = *(reinterpret_cast
                                          <SetI2cAddressRequest *>
                                          (&buffer[1]));
    
            SetI2cAddressResponse response;

            response.result =
            obj_.set_i2c_address(request.address);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SetI2cAddressResponse &output = *(reinterpret_cast
                                                 <SetI2cAddressResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

        case CMD_TEST_METHOD:
          {
            /* Cast buffer as request. */
            TestMethodRequest &request = *(reinterpret_cast
                                          <TestMethodRequest *>
                                          (&buffer[1]));
    
            TestMethodResponse response;

            response.result =
            obj_.test_method();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            TestMethodResponse &output = *(reinterpret_cast
                                                 <TestMethodResponse *>
                                                 (&buffer[0]));
            output = response;
            bytes_written += sizeof(output);
          }
          break;

      default:
        bytes_written = -1;
    }
    return bytes_written;
  }
};

}  // namespace demo_rpc

#endif  // ifndef ___DEMO_RPC___
