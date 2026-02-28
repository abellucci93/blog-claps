import factory

from src.web.api.claps.schemas import ClapsCreateRequest, ClapsGetCountRequest


class ClapsCreateRequestFactory(factory.Factory):
    class Meta:
        model = ClapsCreateRequest

    identifier = factory.Faker("uuid4")


class ClapsGetCountRequestFactory(factory.Factory):
    class Meta:
        model = ClapsGetCountRequest

    identifier = factory.Faker("uuid4")
