'''
Manage transforms for an Azure Media Services account.
'''
from ... pyaz_utils import _call_az
from . import output


def show(account_name, name, resource_group):
    '''
    Show the details of a transform.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the transform.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams transform show", locals())


def list(account_name, resource_group, filter=None, orderby=None):
    '''
    List all the transforms of an Azure Media Services account.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - filter -- Restricts the set of items returned.
    - orderby -- Specifies the key by which the result collection should be ordered.
    '''
    return _call_az("az ams transform list", locals())


def delete(account_name, name, resource_group):
    '''
    Delete a transform.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the transform.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az ams transform delete", locals())


def create(account_name, name, preset, resource_group, audio_analysis_mode=None, audio_language=None, description=None, insights_to_extract=None, on_error=None, relative_priority=None, resolution=None, video_analysis_mode=None):
    '''
    Create a transform.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the transform.
    - preset -- Preset that describes the operations that will be used to modify, transcode, or extract insights from the source file to generate the transform output. Allowed values: H264SingleBitrateSD, H264SingleBitrate720p, H264SingleBitrate1080p, AdaptiveStreaming, AACGoodQualityAudio, ContentAwareEncodingExperimental, ContentAwareEncoding, CopyAllBitrateNonInterleaved, H264MultipleBitrate1080p, H264MultipleBitrate720p, H264MultipleBitrateSD, H265ContentAwareEncoding, H265AdaptiveStreaming, H265SingleBitrate720p, H265SingleBitrate1080p, H265SingleBitrate4K, AudioAnalyzer, VideoAnalyzer, FaceDetector. In addition to the allowed values, you can also pass a path to a custom Standard Encoder preset JSON file. See https://docs.microsoft.com/rest/api/media/transforms/createorupdate#standardencoderpreset for further details on the settings to use to build a custom preset.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - audio_analysis_mode -- Determines the set of audio analysis operations to be performed. If unspecified, the Standard AudioAnalysisMode would be chosen. Allowed values: Standard, Basic.
    - audio_language -- The language for the audio payload in the input using the BCP-47 format of "language tag-region" (e.g: en-US). If not specified, automatic language detection would be employed. This feature currently supports English, Chinese, French, German, Italian, Japanese, Spanish, Russian, and Portuguese. The automatic detection works best with audio recordings with clearly discernable speech. If automatic detection fails to find the language, transcription would fallback to English. Allowed values: en-US, en-GB, es-ES, es-MX, fr-FR, it-IT, ja-JP, pt-BR, zh-CN, de-DE, ar-EG, ru-RU, hi-IN.
    - description -- The description of the transform.
    - insights_to_extract -- The type of insights to be extracted. If not set then the type will be selected based on the content type. If the content is audio only then only audio insights will be extracted and if it is video only video insights will be extracted.
    - on_error -- A Transform can define more than one output. This property defines what the service should do when one output fails - either continue to produce other outputs, or, stop the other outputs. The overall Job state will not reflect failures of outputs that are specified with 'ContinueJob'. The default is 'StopProcessingJob'.
    - relative_priority -- Sets the relative priority of the transform outputs within a transform. This sets the priority that the service uses for processing TransformOutputs. The default priority is Normal.
    - resolution -- Specifies the maximum resolution at which your video is analyzed. The default behavior is "SourceResolution," which will keep the input video at its original resolution when analyzed. Using StandardDefinition will resize input videos to standard definition while preserving the appropriate aspect ratio. It will only resize if the video is of higher resolution. For example, a 1920x1080 input would be scaled to 640x360 before processing. Switching to "StandardDefinition" will reduce the time it takes to process high resolution video. It may also reduce the cost of using this component (see https://azure.microsoft.com/pricing/details/media-services/#analytics for details). However, faces that end up being too small in the resized video may not be detected. Allowed values: StandardDefinition, SourceResolution.
    - video_analysis_mode -- Determines the set of audio analysis operations to be performed. If unspecified, the Standard AudioAnalysisMode would be chosen. Allowed values: Standard, Basic
    '''
    return _call_az("az ams transform create", locals())


def update(account_name, name, resource_group, add=None, description=None, force_string=None, remove=None, set=None):
    '''
    Update the details of a transform.

    Required Parameters:
    - account_name -- The name of the Azure Media Services account.
    - name -- The name of the transform.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - description -- The description of the transform.
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az ams transform update", locals())

