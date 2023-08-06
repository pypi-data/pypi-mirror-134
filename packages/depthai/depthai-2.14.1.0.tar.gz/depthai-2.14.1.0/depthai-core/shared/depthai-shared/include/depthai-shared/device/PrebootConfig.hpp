#pragma once

// std
#include <cstdint>

// project
#include "depthai-shared/common/UsbSpeed.hpp"
#include "depthai-shared/common/optional.hpp"
#include "depthai-shared/utility/Serialization.hpp"
#include "depthai-shared/xlink/XLinkConstants.hpp"

namespace dai {

constexpr static uint32_t PREBOOT_CONFIG_MAGIC1 = 0x78010000U;
constexpr static uint32_t PREBOOT_CONFIG_MAGIC2 = 0x21ea17e6U;

struct PrebootConfig {
    // USB related config
    struct USB {
        uint16_t vid = 0x03e7, pid = 0xf63b;
        uint16_t flashBootedVid = 0x03e7, flashBootedPid = 0xf63d;
        UsbSpeed maxSpeed = UsbSpeed::SUPER;
    };

    USB usb;
    tl::optional<uint32_t> watchdogTimeoutMs;
    tl::optional<uint32_t> watchdogInitialDelayMs;
};

DEPTHAI_SERIALIZE_EXT(PrebootConfig::USB, vid, pid, flashBootedVid, flashBootedPid, maxSpeed);
DEPTHAI_SERIALIZE_EXT(PrebootConfig, usb, watchdogTimeoutMs, watchdogInitialDelayMs);

}  // namespace dai
