#include <stdint.h>

class Bar {
  uint8_t value();
};


namespace world {

template <uint32_t PacketSize, uint8_t Type=1>
class Foo {
public:
  uint8_t bar_;

  int32_t foo_bar() {}
};

} // namespace world
