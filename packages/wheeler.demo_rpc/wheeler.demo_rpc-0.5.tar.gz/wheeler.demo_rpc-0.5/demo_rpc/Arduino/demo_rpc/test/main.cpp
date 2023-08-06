//#define LOGGING
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include "pb_validate.h"
#include "demo_rpc_config_validate.h"
#include "demo_rpc_config_pb.h"


int main(int argc, char const* argv[]) {
  Config config = Config_init_default;
  Config config2 = Config_init_default;

  if (argc > 3) {
    std::cerr << "usage: " << argv[0] << " [serial_number] [i2c_address]"
      << std::endl;
    return -1;
  }
  if (argc > 1) {
    config.serial_number = atoi(argv[1]);
    config.has_serial_number = true;
  }
  if (argc > 2) {
    config.i2c_address = atoi(argv[2]);
    config.has_i2c_address = true;
  }

  config2.serial_number = 42;
  config2.has_serial_number = true;
  config2.i2c_address = 10;
  config2.has_i2c_address = true;

  MessageValidator<2> validator;
  SerialNumberValidator serial_number_validator;
  I2cAddressValidator i2c_address_validator;

  validator.register_validator(serial_number_validator);
  validator.register_validator(i2c_address_validator);

  validator.update(Config_fields, config, config2);

  std::cout << "config: serial_number=" << config.serial_number
    << ", i2c_address=" << config.i2c_address << std::endl;
  std::cout << "config2: serial_number=" << config2.serial_number
    << ", i2c_address=" << config2.i2c_address << std::endl;

  return 0;
}
