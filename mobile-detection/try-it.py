from FiftyOneDegrees import fiftyone_degrees_mobile_detector_v3_wrapper
from fiftyone_degrees.mobile_detector.conf import settings
import sys


dataFile = settings.V3_WRAPPER_DATABASE
properties = settings.PROPERTIES
cacheSize = settings.CACHE_SIZE
poolSize = settings.POOL_SIZE

'''
Initialises the device detection provider with settings from the settings
file. By default this will use the included Lite data file For more info
see:
<a href="https://51degrees.com/compare-data-options">compare data options
</a>
'''
provider = fiftyone_degrees_mobile_detector_v3_wrapper.Provider(dataFile,
    properties,
    cacheSize,
    poolSize)

# User-Agent string of an iPhone mobile device.
mobileUserAgent = ("Mozilla/5.0 (iPhone; CPU iPhone OS 7_1 like Mac OS X) "
"AppleWebKit/537.51.2 (KHTML, like Gecko) 'Version/7.0 Mobile/11D167 "
"Safari/9537.53")

# User-Agent string of Firefox Web browser version 41 on desktop.
desktopUserAgent = ("Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) "
"Gecko/20100101 Firefox/41.0")

# User-Agent string of a MediaHub device.
mediaHubUserAgent = ("Mozilla/5.0 (Linux; Android 4.4.2; X7 Quad Core "
"Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
"Chrome/30.0.0.0 Safari/537.36")

def main():
    sys.stdout.write('Starting Getting Started Example.\n')

# Carries out a match with a mobile User-Agent.
    sys.stdout.write('\nMobile User-Agent: %s\n' % mobileUserAgent)
    match = provider.getMatch(mobileUserAgent)
    sys.stdout.write('   IsMobile: %s\n' % match.getValues('IsMobile'))

# Carries out a match with a desktop User-Agent.
    sys.stdout.write('\nDesktop User-Agent: %s\n' % desktopUserAgent)
    match = provider.getMatch(desktopUserAgent)
    sys.stdout.write('   IsMobile: %s\n' % match.getValues('IsMobile'))

# Carries out a match with a MediaHub User-Agent.
    sys.stdout.write('\nMedia Hub User-Agent: %s\n' % mediaHubUserAgent)
    match = provider.getMatch(mediaHubUserAgent)
    sys.stdout.write('   IsMobile: %s\n' % match.getValues('IsMobile'))

if __name__ == '__main__':
    main()