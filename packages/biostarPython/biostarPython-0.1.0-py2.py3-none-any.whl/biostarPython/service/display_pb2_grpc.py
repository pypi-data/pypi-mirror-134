# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from biostarPython.service import display_pb2 as display__pb2


class DisplayStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.UpdateLanguagePack = channel.unary_unary(
        '/display.Display/UpdateLanguagePack',
        request_serializer=display__pb2.UpdateLanguagePackRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateLanguagePackResponse.FromString,
        )
    self.UpdateLanguagePackMulti = channel.unary_unary(
        '/display.Display/UpdateLanguagePackMulti',
        request_serializer=display__pb2.UpdateLanguagePackMultiRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateLanguagePackMultiResponse.FromString,
        )
    self.UpdateNotice = channel.unary_unary(
        '/display.Display/UpdateNotice',
        request_serializer=display__pb2.UpdateNoticeRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateNoticeResponse.FromString,
        )
    self.UpdateNoticeMulti = channel.unary_unary(
        '/display.Display/UpdateNoticeMulti',
        request_serializer=display__pb2.UpdateNoticeMultiRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateNoticeMultiResponse.FromString,
        )
    self.UpdateBackgroundImage = channel.unary_unary(
        '/display.Display/UpdateBackgroundImage',
        request_serializer=display__pb2.UpdateBackgroundImageRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateBackgroundImageResponse.FromString,
        )
    self.UpdateBackgroundImageMulti = channel.unary_unary(
        '/display.Display/UpdateBackgroundImageMulti',
        request_serializer=display__pb2.UpdateBackgroundImageMultiRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateBackgroundImageMultiResponse.FromString,
        )
    self.UpdateSlideImages = channel.unary_unary(
        '/display.Display/UpdateSlideImages',
        request_serializer=display__pb2.UpdateSlideImagesRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateSlideImagesResponse.FromString,
        )
    self.UpdateSlideImagesMulti = channel.unary_unary(
        '/display.Display/UpdateSlideImagesMulti',
        request_serializer=display__pb2.UpdateSlideImagesMultiRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateSlideImagesMultiResponse.FromString,
        )
    self.UpdateSound = channel.unary_unary(
        '/display.Display/UpdateSound',
        request_serializer=display__pb2.UpdateSoundRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateSoundResponse.FromString,
        )
    self.UpdateSoundMulti = channel.unary_unary(
        '/display.Display/UpdateSoundMulti',
        request_serializer=display__pb2.UpdateSoundMultiRequest.SerializeToString,
        response_deserializer=display__pb2.UpdateSoundMultiResponse.FromString,
        )
    self.GetConfig = channel.unary_unary(
        '/display.Display/GetConfig',
        request_serializer=display__pb2.GetConfigRequest.SerializeToString,
        response_deserializer=display__pb2.GetConfigResponse.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/display.Display/SetConfig',
        request_serializer=display__pb2.SetConfigRequest.SerializeToString,
        response_deserializer=display__pb2.SetConfigResponse.FromString,
        )
    self.SetConfigMulti = channel.unary_unary(
        '/display.Display/SetConfigMulti',
        request_serializer=display__pb2.SetConfigMultiRequest.SerializeToString,
        response_deserializer=display__pb2.SetConfigMultiResponse.FromString,
        )


class DisplayServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def UpdateLanguagePack(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateLanguagePackMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateNotice(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateNoticeMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateBackgroundImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateBackgroundImageMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSlideImages(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSlideImagesMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSound(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSoundMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfigMulti(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DisplayServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'UpdateLanguagePack': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLanguagePack,
          request_deserializer=display__pb2.UpdateLanguagePackRequest.FromString,
          response_serializer=display__pb2.UpdateLanguagePackResponse.SerializeToString,
      ),
      'UpdateLanguagePackMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateLanguagePackMulti,
          request_deserializer=display__pb2.UpdateLanguagePackMultiRequest.FromString,
          response_serializer=display__pb2.UpdateLanguagePackMultiResponse.SerializeToString,
      ),
      'UpdateNotice': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateNotice,
          request_deserializer=display__pb2.UpdateNoticeRequest.FromString,
          response_serializer=display__pb2.UpdateNoticeResponse.SerializeToString,
      ),
      'UpdateNoticeMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateNoticeMulti,
          request_deserializer=display__pb2.UpdateNoticeMultiRequest.FromString,
          response_serializer=display__pb2.UpdateNoticeMultiResponse.SerializeToString,
      ),
      'UpdateBackgroundImage': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateBackgroundImage,
          request_deserializer=display__pb2.UpdateBackgroundImageRequest.FromString,
          response_serializer=display__pb2.UpdateBackgroundImageResponse.SerializeToString,
      ),
      'UpdateBackgroundImageMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateBackgroundImageMulti,
          request_deserializer=display__pb2.UpdateBackgroundImageMultiRequest.FromString,
          response_serializer=display__pb2.UpdateBackgroundImageMultiResponse.SerializeToString,
      ),
      'UpdateSlideImages': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSlideImages,
          request_deserializer=display__pb2.UpdateSlideImagesRequest.FromString,
          response_serializer=display__pb2.UpdateSlideImagesResponse.SerializeToString,
      ),
      'UpdateSlideImagesMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSlideImagesMulti,
          request_deserializer=display__pb2.UpdateSlideImagesMultiRequest.FromString,
          response_serializer=display__pb2.UpdateSlideImagesMultiResponse.SerializeToString,
      ),
      'UpdateSound': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSound,
          request_deserializer=display__pb2.UpdateSoundRequest.FromString,
          response_serializer=display__pb2.UpdateSoundResponse.SerializeToString,
      ),
      'UpdateSoundMulti': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSoundMulti,
          request_deserializer=display__pb2.UpdateSoundMultiRequest.FromString,
          response_serializer=display__pb2.UpdateSoundMultiResponse.SerializeToString,
      ),
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=display__pb2.GetConfigRequest.FromString,
          response_serializer=display__pb2.GetConfigResponse.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=display__pb2.SetConfigRequest.FromString,
          response_serializer=display__pb2.SetConfigResponse.SerializeToString,
      ),
      'SetConfigMulti': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfigMulti,
          request_deserializer=display__pb2.SetConfigMultiRequest.FromString,
          response_serializer=display__pb2.SetConfigMultiResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'display.Display', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
