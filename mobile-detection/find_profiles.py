from FiftyOneDegrees import fiftyone_degrees_mobile_detector_v3_wrapper
from fiftyone_degrees.mobile_detector.conf import settings
import sys

'''
Imports settings from the settings file. The Default settings file, and
details on how to change it can be output by running the command
<p><pre class="prettyprint lang-py">
51degrees-mobile-detector settings
</p></pre>
'''
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

def main():
    print ("Starting Find Profiles Example.\n")

    # Retrive all the mobile profiles from the data set.
    profiles = provider.findProfiles("IsMobile", "True")
    print ()
    print ("There are %d mobile profiles in the %s data file." % (profiles.getCount(), provider.getDataSetName()))
    profiles = provider.findProfiles("ScreenPixelsWidth", "1080", profiles)
    print ("%d of them have a screen width of 1080 pixels." % profiles.getCount())

    # Retrieve all the non-mobile profiles from the data set.
    profiles = provider.findProfiles("IsMobile", "False")
    print ("There are %d non-mobile profiles in the %s data file." % (profiles.getCount(), provider.getDataSetName()))
    profiles = provider.findProfiles("ScreenPixelsWidth", "1080", profiles)
    print ("%d of them have a screen width of 1080 pixels." % profiles.getCount())

if __name__ == '__main__':
    main()