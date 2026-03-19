import tinytuya
import time
import json


class TuyaDeviceController:
    def __init__(self, dev_id, address, local_key, version=3.4):
        """Initialize Tuya device controller"""
        self.device = tinytuya.OutletDevice(
            dev_id='bfe90802d000270bdefwk3',
            address='192.168.30.116',  # Auto-discover IP
            local_key='R>ibtHCe#GRfM?C6',
            version=3.4
        )
        self.dev_id = dev_id
        self.device.set_socketTimeout(5)
        
    def get_status(self):
        """Get current device status"""
        try:
            data = self.device.status()
            if data and 'dps' in data:
                print(f"✓ Device Status:")
                for key, value in data['dps'].items():
                    print(f"  DPS {key}: {value}")
                return data
            else:
                print(f"⚠ Response: {data}")
                return data
        except Exception as e:
            print(f"❌ Error getting status: {e}")
            return None
    
    def is_on(self):
        """Check if device is currently on"""
        status = self.get_status()
        if status and 'dps' in status:
            # Check main switch (usually DPS 1)
            return status['dps'].get('1', False)
        return False
    
    def turn_on(self, switch=1):
        """Turn device on
        
        Args:
            switch: Which switch to control (1 or 2 for 2-gang switches)
        """
        try:
            result = self.device.turn_on(switch=switch)
            print(f"✓ Turned ON (switch {switch})")
            time.sleep(0.5)
            return self.get_status()
        except Exception as e:
            print(f"❌ Error turning on: {e}")
            return None
    
    def turn_off(self, switch=1):
        """Turn device off
        
        Args:
            switch: Which switch to control (1 or 2 for 2-gang switches)
        """
        try:
            result = self.device.turn_off(switch=switch)
            print(f"✓ Turned OFF (switch {switch})")
            time.sleep(0.5)
            return self.get_status()
        except Exception as e:
            print(f"❌ Error turning off: {e}")
            return None
    
    def toggle(self, switch=1):
        """Toggle device state"""
        status = self.get_status()
        if status and 'dps' in status:
            current_state = status['dps'].get(str(switch), False)
            if current_state:
                print(f"Device switch {switch} is ON, turning OFF...")
                return self.turn_off(switch)
            else:
                print(f"Device switch {switch} is OFF, turning ON...")
                return self.turn_on(switch)
        return None
    
    def set_timer(self, seconds, switch=1):
        """Set countdown timer
        
        Args:
            seconds: Number of seconds until auto-off (0 to disable)
            switch: Which switch (1 or 2)
        """
        try:
            # DPS 9 is usually the countdown timer
            dps_key = 9 if switch == 1 else 10
            result = self.device.set_value(dps_key, seconds)
            print(f"✓ Timer set to {seconds} seconds for switch {switch}")
            return result
        except Exception as e:
            print(f"❌ Error setting timer: {e}")
            return None
    
    def get_dps_value(self, dps_key):
        """Get specific DPS (Data Point) value"""
        status = self.get_status()
        if status and 'dps' in status:
            return status['dps'].get(str(dps_key))
        return None
    
    def set_dps_value(self, dps_key, value):
        """Set specific DPS value"""
        try:
            result = self.device.set_value(dps_key, value)
            print(f"✓ Set DPS {dps_key} to {value}")
            time.sleep(0.3)
            return self.get_status()
        except Exception as e:
            print(f"❌ Error setting DPS: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize your device with the correct credentials
    controller = TuyaDeviceController(
        dev_id='E86BEAEAF5F8',
        address='192.168.30.116',  # Auto-discover IP
        local_key='R>ibtHCe#GRfM?C6',
        version=3.4
    )
    
    print("="*60)
    print("TUYA DEVICE CONTROLLER")
    print("="*60)
    print()
    
    # Get initial status
    print("📊 Initial Status:")
    controller.get_status()
    print()
    


    print("🔴 Turning device OFF...")
    controller.turn_off(switch=1)
    controller.turn_off(switch=2)
    time.sleep(5)
    print()
    # Turn on
    print("🔛 Turning device ON...")
    controller.turn_on(switch=2)
    print()
    
    # Wait
    print("⏳ Waiting 5 seconds...")
    time.sleep(5)
    
    # Turn off
    print("🔴 Turning device OFF...")
    #controller.turn_off(switch=2)
    print()
    
    # Toggle example
    print("🔄 Toggling device...")
    controller.toggle()
    print()
    
    # Set a 10-second timer (device will auto-off after 10 seconds)
    # Uncomment if you want to test timer:
    # print("⏲️  Setting 10-second timer...")
    # controller.set_timer(10)
    
    print("="*60)
    print("✅ All tests complete!")
    print("......................")
    print("💡 Your device is working! What would you like to build?")
    print("   1. Web dashboard")
    print("   2. Automation/scheduling")
    print("   3. Multi-device control")
    print("   4. Voice assistant integration")
    