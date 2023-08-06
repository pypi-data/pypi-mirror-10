#ifndef ___DEMO_RPC___
#define ___DEMO_RPC___

#include "Array.h"
#include "remote_i2c_command.h"


#define BASE_NODE__NAME  ("demo_rpc")
#define BASE_NODE__MANUFACTURER  ("Wheeler Lab")
#define BASE_NODE__SOFTWARE_VERSION  ("0.4")
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

struct I2cSendCommandRequest {
  uint8_t address;
  UInt8Array payload;
};

struct I2cSendCommandResponse {
  UInt8Array result;
};

struct I2cCommandReadRequest {
  uint8_t address;
};

struct I2cCommandReadResponse {
  UInt8Array result;
};

struct SetSpiBitOrderRequest {
  uint8_t order;
};

struct SetSpiBitOrderResponse {
};

struct SetSpiClockDividerRequest {
  uint8_t divider;
};

struct SetSpiClockDividerResponse {
};

struct SetSpiDataModeRequest {
  uint8_t mode;
};

struct SetSpiDataModeResponse {
};

struct SpiTransferRequest {
  uint8_t value;
};

struct SpiTransferResponse {
  uint8_t result;
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
    static const int CMD_I2C_BUFFER_SIZE = 0x10;
    static const int CMD_I2C_SCAN = 0x11;
    static const int CMD_I2C_AVAILABLE = 0x12;
    static const int CMD_I2C_READ_BYTE = 0x13;
    static const int CMD_I2C_REQUEST_FROM = 0x14;
    static const int CMD_I2C_READ = 0x15;
    static const int CMD_I2C_WRITE = 0x16;
    static const int CMD_I2C_SEND_COMMAND = 0x17;
    static const int CMD_I2C_COMMAND_READ = 0x18;
    static const int CMD_SET_SPI_BIT_ORDER = 0x19;
    static const int CMD_SET_SPI_CLOCK_DIVIDER = 0x1a;
    static const int CMD_SET_SPI_DATA_MODE = 0x1b;
    static const int CMD_SPI_TRANSFER = 0x1c;
    static const int CMD_NAME = 0x1d;
    static const int CMD_MANUFACTURER = 0x1e;
    static const int CMD_SOFTWARE_VERSION = 0x1f;
    static const int CMD_URL = 0x20;
    static const int CMD_TEST_METHOD = 0x30;

  UInt8Array process_command(uint16_t request_size, uint16_t buffer_size,
                             uint8_t *buffer) {
    /* ## Call operator ##
     *
     * Arguments:
     *
     *  - `request`: Protocol buffer command request structure,
     *  - `buffer_size`: The number of bytes in the arguments buffer.
     *  - `data`: The arguments buffer. */
    uint8_t command = buffer[0];
    UInt8Array result;

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
            result.data = buffer;
            result.length = sizeof(output);
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
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_DELAY_US:
          {
            /* Cast buffer as request. */
            DelayUsRequest &request = *(reinterpret_cast
                                          <DelayUsRequest *>
                                          (&buffer[1]));
    
            obj_.delay_us(request.us);
    
        result.data = buffer;
        result.length = 0;
          }
          break;

        case CMD_DELAY_MS:
          {
            /* Cast buffer as request. */
            DelayMsRequest &request = *(reinterpret_cast
                                          <DelayMsRequest *>
                                          (&buffer[1]));
    
            obj_.delay_ms(request.ms);
    
        result.data = buffer;
        result.length = 0;
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
            result.data = buffer;
            result.length = sizeof(output);
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
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_PIN_MODE:
          {
            /* Cast buffer as request. */
            PinModeRequest &request = *(reinterpret_cast
                                          <PinModeRequest *>
                                          (&buffer[1]));
    
            obj_.pin_mode(request.pin, request.mode);
    
        result.data = buffer;
        result.length = 0;
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
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_DIGITAL_WRITE:
          {
            /* Cast buffer as request. */
            DigitalWriteRequest &request = *(reinterpret_cast
                                          <DigitalWriteRequest *>
                                          (&buffer[1]));
    
            obj_.digital_write(request.pin, request.value);
    
        result.data = buffer;
        result.length = 0;
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
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_ANALOG_WRITE:
          {
            /* Cast buffer as request. */
            AnalogWriteRequest &request = *(reinterpret_cast
                                          <AnalogWriteRequest *>
                                          (&buffer[1]));
    
            obj_.analog_write(request.pin, request.value);
    
        result.data = buffer;
        result.length = 0;
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
            result.data = buffer;
            result.length = sizeof(output);
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

            result.data = (uint8_t *)response.result.data;
            result.length = length;
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

            result.data = (uint8_t *)response.result.data;
            result.length = length;
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
            result.data = buffer;
            result.length = sizeof(output);
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
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_BUFFER_SIZE:
          {
            /* Cast buffer as request. */
            I2cBufferSizeRequest &request = *(reinterpret_cast
                                          <I2cBufferSizeRequest *>
                                          (&buffer[1]));
    
            I2cBufferSizeResponse response;

            response.result =
            obj_.i2c_buffer_size();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cBufferSizeResponse &output = *(reinterpret_cast
                                                 <I2cBufferSizeResponse *>
                                                 (&buffer[0]));
            output = response;
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_SCAN:
          {
            /* Cast buffer as request. */
            I2cScanRequest &request = *(reinterpret_cast
                                          <I2cScanRequest *>
                                          (&buffer[1]));
    
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
                                          (&buffer[1]));
    
            I2cAvailableResponse response;

            response.result =
            obj_.i2c_available();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cAvailableResponse &output = *(reinterpret_cast
                                                 <I2cAvailableResponse *>
                                                 (&buffer[0]));
            output = response;
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_READ_BYTE:
          {
            /* Cast buffer as request. */
            I2cReadByteRequest &request = *(reinterpret_cast
                                          <I2cReadByteRequest *>
                                          (&buffer[1]));
    
            I2cReadByteResponse response;

            response.result =
            obj_.i2c_read_byte();
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cReadByteResponse &output = *(reinterpret_cast
                                                 <I2cReadByteResponse *>
                                                 (&buffer[0]));
            output = response;
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_REQUEST_FROM:
          {
            /* Cast buffer as request. */
            I2cRequestFromRequest &request = *(reinterpret_cast
                                          <I2cRequestFromRequest *>
                                          (&buffer[1]));
    
            I2cRequestFromResponse response;

            response.result =
            obj_.i2c_request_from(request.address, request.n_bytes_to_read);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            I2cRequestFromResponse &output = *(reinterpret_cast
                                                 <I2cRequestFromResponse *>
                                                 (&buffer[0]));
            output = response;
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_I2C_READ:
          {
            /* Cast buffer as request. */
            I2cReadRequest &request = *(reinterpret_cast
                                          <I2cReadRequest *>
                                          (&buffer[1]));
    
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
                                          (&buffer[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.data.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.data.data);
            obj_.i2c_write(request.address, request.data);
    
        result.data = buffer;
        result.length = 0;
          }
          break;

        case CMD_I2C_SEND_COMMAND:
          {
            /* Cast buffer as request. */
            I2cSendCommandRequest &request = *(reinterpret_cast
                                          <I2cSendCommandRequest *>
                                          (&buffer[1]));
    
            /* Add relative array data offsets to start payload structure. */
    
            request.payload.data = (uint8_t *)((uint8_t *)&request + (uint16_t)request.payload.data);
            I2cSendCommandResponse response;

            response.result =
            obj_.i2c_send_command(request.address, request.payload);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_I2C_COMMAND_READ:
          {
            /* Cast buffer as request. */
            I2cCommandReadRequest &request = *(reinterpret_cast
                                          <I2cCommandReadRequest *>
                                          (&buffer[1]));
    
            I2cCommandReadResponse response;

            response.result =
            obj_.i2c_command_read(request.address);
    
            /* Copy result to output buffer. */
            /* Result type is an array, so need to do `memcpy` for array data. */
            uint16_t length = (response.result.length *
                               sizeof(response.result.data[0]));

            result.data = (uint8_t *)response.result.data;
            result.length = length;
          }
          break;

        case CMD_SET_SPI_BIT_ORDER:
          {
            /* Cast buffer as request. */
            SetSpiBitOrderRequest &request = *(reinterpret_cast
                                          <SetSpiBitOrderRequest *>
                                          (&buffer[1]));
    
            obj_.set_spi_bit_order(request.order);
    
        result.data = buffer;
        result.length = 0;
          }
          break;

        case CMD_SET_SPI_CLOCK_DIVIDER:
          {
            /* Cast buffer as request. */
            SetSpiClockDividerRequest &request = *(reinterpret_cast
                                          <SetSpiClockDividerRequest *>
                                          (&buffer[1]));
    
            obj_.set_spi_clock_divider(request.divider);
    
        result.data = buffer;
        result.length = 0;
          }
          break;

        case CMD_SET_SPI_DATA_MODE:
          {
            /* Cast buffer as request. */
            SetSpiDataModeRequest &request = *(reinterpret_cast
                                          <SetSpiDataModeRequest *>
                                          (&buffer[1]));
    
            obj_.set_spi_data_mode(request.mode);
    
        result.data = buffer;
        result.length = 0;
          }
          break;

        case CMD_SPI_TRANSFER:
          {
            /* Cast buffer as request. */
            SpiTransferRequest &request = *(reinterpret_cast
                                          <SpiTransferRequest *>
                                          (&buffer[1]));
    
            SpiTransferResponse response;

            response.result =
            obj_.spi_transfer(request.value);
    
            /* Copy result to output buffer. */
            /* Cast start of buffer as reference of result type and assign result. */
            SpiTransferResponse &output = *(reinterpret_cast
                                                 <SpiTransferResponse *>
                                                 (&buffer[0]));
            output = response;
            result.data = buffer;
            result.length = sizeof(output);
          }
          break;

        case CMD_NAME:
          {
            /* Cast buffer as request. */
            NameRequest &request = *(reinterpret_cast
                                          <NameRequest *>
                                          (&buffer[1]));
    
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
                                          (&buffer[1]));
    
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
                                          (&buffer[1]));
    
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
                                          (&buffer[1]));
    
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
            result.data = buffer;
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
