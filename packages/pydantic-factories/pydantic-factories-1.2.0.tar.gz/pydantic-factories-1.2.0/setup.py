# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_factories',
 'pydantic_factories.constraints',
 'pydantic_factories.extensions',
 'pydantic_factories.value_generators']

package_data = \
{'': ['*']}

install_requires = \
['exrex', 'faker', 'pydantic', 'typing-extensions']

setup_kwargs = {
    'name': 'pydantic-factories',
    'version': '1.2.0',
    'description': 'Mock data generation for pydantic based models',
    'long_description': '<div align="center">\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pydantic-factories)\n\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_pydantic-factories&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Goldziher_pydantic-factories)\n[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_pydantic-factories&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_pydantic-factories)\n[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_pydantic-factories&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Goldziher_pydantic-factories)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Goldziher_pydantic-factories&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Goldziher_pydantic-factories)\n\n[![Discord](https://img.shields.io/discord/919193495116337154?color=blue&label=chat%20on%20discord&logo=discord)](https://discord.gg/X3FJqy8d2j)\n\n</div>\n\n# Pydantic-Factories\n\nThis library offers powerful mock data generation capabilities for [pydantic](https://github.com/samuelcolvin/pydantic)\nbased models and `dataclasses`. It can also be used with other libraries that use pydantic as a foundation, for\nexample [SQLModel](https://github.com/tiangolo/sqlmodel) and [Beanie](https://github.com/roman-right/beanie).\n\n### Example\n\n```python\nfrom datetime import date, datetime\nfrom typing import List, Union\n\nfrom pydantic import BaseModel, UUID4\n\nfrom pydantic_factories import ModelFactory\n\n\nclass Person(BaseModel):\n    id: UUID4\n    name: str\n    hobbies: List[str]\n    age: Union[float, int]\n    birthday: Union[datetime, date]\n\n\nclass PersonFactory(ModelFactory):\n    __model__ = Person\n\n\nresult = PersonFactory.build()\n```\n\nThat\'s it - with almost no work, we are able to create a mock data object fitting the `Person` class model definition.\n\nThis is possible because of the typing information available on the pydantic model and model-fields, which are used as a\nsource of truth for data generation.\n\nThe factory parses the information stored in the pydantic model and generates a dictionary of kwargs that are passed to\nthe `Person` class\' init method.\n\n### Features\n\n- ✅ supports both built-in and pydantic types\n- ✅ supports pydantic field constraints\n- ✅ supports complex field types\n- ✅ supports custom model fields\n\n### Why This Library?\n\n- 💯 powerful\n- 💯 extensible\n- 💯 simple\n- 💯 rigorously tested\n\n## Installation\n\nUsing your package manager of choice:\n\n```sh\npip install pydantic-factories\n```\n\nOR\n\n```sh\npoetry add --dev pydantic-factories\n```\n\nOR\n\n```sh\npipenv install --dev pydantic-factories\n```\n\n**pydantic-factories** has very few dependencies aside from _pydantic_ - [\ntyping-extensions](https://github.com/python/typing/blob/master/typing_extensions/README.rst) which is used for typing\nsupport in older versions of python, as well as [faker](https://github.com/joke2k/faker)\nand [exrex](https://github.com/asciimoo/exrex), both of which are used for generating mock data.\n\n## Usage\n\n### Build Methods\n\nThe `ModelFactory` class exposes two build methods:\n\n- `.build(**kwargs)` - builds a single instance of the factory\'s model\n- `.batch(size: int, **kwargs)` - build a list of size n instances\n\n```python\nresult = PersonFactory.build()  # a single Person instance\n\nresult = PersonFactory.batch(size=5)  # list[Person, Person, Person, Person, Person]\n```\n\nAny `kwargs` you pass to `.build`, `.batch` or any of the [persistence methods](#persistence), will take precedence over\nwhatever defaults are defined on the factory class itself.\n\nBy default, when building a pydantic class, kwargs are validated, to avoid input validation you can use the `factory_use_construct` param.\n```python\nresult = PersonFactory.build(id=5)  # Raises a validation error\n\nresult = PersonFactory.build(\n    factory_use_construct=True, id=5\n)  # Build a Person with invalid id\n```\n\n### Nested Models and Complex types\n\nThe automatic generation of mock data works for all types supported by pydantic, as well as nested classes that derive\nfrom `BaseModel` (including for 3rd party libraries) and complex types. Let\'s look at another example:\n\n```python\nfrom datetime import date, datetime\nfrom enum import Enum\nfrom pydantic import BaseModel, UUID4\nfrom typing import Any, Dict, List, Union\n\nfrom pydantic_factories import ModelFactory\n\n\nclass Species(str, Enum):\n    CAT = "Cat"\n    DOG = "Dog"\n    PIG = "Pig"\n    MONKEY = "Monkey"\n\n\nclass Pet(BaseModel):\n    name: str\n    sound: str\n    species: Species\n\n\nclass Person(BaseModel):\n    id: UUID4\n    name: str\n    hobbies: List[str]\n    age: Union[float, int]\n    birthday: Union[datetime, date]\n    pets: List[Pet]\n    assets: List[Dict[str, Dict[str, Any]]]\n\n\nclass PersonFactory(ModelFactory):\n    __model__ = Person\n\n\nresult = PersonFactory.build()\n```\n\nThis example will also work out of the box although no factory was defined for the Pet class, that\'s not a problem - a\nfactory will be dynamically generated for it on the fly.\n\nThe complex typing under the `assets` attribute is a bit more tricky, but the factory will generate a python object\nfitting this signature, therefore passing validation.\n\n**Please note**: the one thing factories cannot handle is self referencing models, because this can lead to recursion\nerrors. In this case you will need to handle the particular field by setting defaults for it.\n\n### Models and Dataclasses\n\nThis library works with any class that inherits the pydantic `BaseModel` class, including `GenericModel` and classes\nfrom 3rd party libraries, and also with dataclasses - both those from the python standard library and pydantic\'s\ndataclasses. In fact, you can use them interchangeably as you like:\n\n```python\nimport dataclasses\nfrom typing import Dict, List\n\nimport pydantic\nfrom pydantic_factories import ModelFactory\n\n\n@pydantic.dataclasses.dataclass\nclass MyPydanticDataClass:\n    name: str\n\n\nclass MyFirstModel(pydantic.BaseModel):\n    dataclass: MyPydanticDataClass\n\n\n@dataclasses.dataclass()\nclass MyPythonDataClass:\n    id: str\n    complex_type: Dict[str, Dict[int, List[MyFirstModel]]]\n\n\nclass MySecondModel(pydantic.BaseModel):\n    dataclasses: List[MyPythonDataClass]\n\n\nclass MyFactory(ModelFactory):\n    __model__ = MySecondModel\n\n\nresult = MyFactory.build()\n```\n\nThe above example will build correctly.\n\n#### Note Regarding Nested Optional Types in Dataclasses\n\nWhen generating mock values for fields typed as `Optional`, if the factory is defined\nwith `__allow_none_optionals__ = True`, the field value will be either a value or None - depending on a random decision.\nThis works even when the `Optional` typing is deeply nested, except for dataclasses - typing is only shallowly evaluated\nfor dataclasses, and as such they are always assumed to require a value. If you wish to have a None value, in this\nparticular case, you should do so manually by configured a `Use` callback for the particular field.\n\n### Factory Configuration\n\nConfiguration of `ModelFactory` is done using class variables:\n\n- **\\_\\_model\\_\\_**: a _required_ variable specifying the model for the factory. It accepts any class that extends _\n  pydantic\'s_ `BaseModel` including classes from other libraries. If this variable is not set,\n  a `ConfigurationException` will be raised.\n\n- **\\_\\_faker\\_\\_**: an _optional_ variable specifying a user configured instance of faker. If this variable is not set,\n  the factory will default to using vanilla `faker`.\n\n- **\\_\\_sync_persistence\\_\\_**: an _optional_ variable specifying the handler for synchronously persisting data. If this\n  is variable is not set, the `.create_sync` and `.create_batch_sync` methods of the factory cannot be used.\n  See: [persistence methods](#persistence)\n\n- **\\_\\_async_persistence\\_\\_**: an _optional_ variable specifying the handler for asynchronously persisting data. If\n  this is variable is not set, the `.create_async` and `.create_batch_async` methods of the factory cannot be used.\n  See: [persistence methods](#persistence)\n\n- **\\_\\_allow_none_optionals_\\_\\_**: an _optional_ variable sepcifying whether the factory should randomly set None\n  values for optional fields, or always set a value for them. This is `True` by default.\n\n```python\nfrom faker import Faker\nfrom pydantic_factories import ModelFactory\n\nfrom app.models import Person\nfrom .persistence import AsyncPersistenceHandler, SyncPersistenceHandler\n\nFaker.seed(5)\nmy_faker = Faker("en-EN")\n\n\nclass PersonFactory(ModelFactory):\n    __model__ = Person\n    __faker__ = my_faker\n    __sync_persistence__ = SyncPersistenceHandler\n    __async_persistence__ = AsyncPersistenceHandler\n    __allow_none_optionals__ = False\n    ...\n```\n#### Generating deterministic objects\n\nIn order to generate determenistic data, use `ModelFactory.seed_random` method. This will pass  the seed value to both\nFaker and random method calls, guaranteeing data to be the same in between the calls. Especially useful for testing.\n\n### Defining Factory Attributes\n\nThe factory api is designed to be as semantic and simple as possible, lets look at several examples that assume we have\nthe following models:\n\n```python\nfrom datetime import date, datetime\nfrom enum import Enum\nfrom pydantic import BaseModel, UUID4\nfrom typing import Any, Dict, List, Union\n\n\nclass Species(str, Enum):\n    CAT = "Cat"\n    DOG = "Dog"\n\n\nclass Pet(BaseModel):\n    name: str\n    species: Species\n\n\nclass Person(BaseModel):\n    id: UUID4\n    name: str\n    hobbies: List[str]\n    age: Union[float, int]\n    birthday: Union[datetime, date]\n    pets: List[Pet]\n    assets: List[Dict[str, Dict[str, Any]]]\n```\n\nOne way of defining defaults is to use hardcoded values:\n\n```python\npet = Pet(name="Roxy", sound="woof woof", species=Species.DOG)\n\n\nclass PersonFactory(ModelFactory):\n    __model__ = Person\n\n    pets = [pet]\n```\n\nIn this case when we call `PersonFactory.build()` the result will be randomly generated, except the pets list, which\nwill be the hardcoded default we defined.\n\n#### Use (field)\n\nThis though is often not desirable. We could instead, define a factory for `Pet` where we restrict the choices to a\nrange we like. For example:\n\n```python\nfrom enum import Enum\nfrom pydantic_factories import ModelFactory, Use\nfrom random import choice\n\nfrom .models import Pet, Person\n\n\nclass Species(str, Enum):\n    CAT = "Cat"\n    DOG = "Dog"\n\n\nclass PetFactory(ModelFactory):\n    __model__ = Pet\n\n    name = Use(choice, ["Ralph", "Roxy"])\n    species = Use(choice, list(Species))\n\n\nclass PersonFactory(ModelFactory):\n    __model__ = Person\n\n    pets = Use(PetFactory.batch, size=2)\n```\n\nThe signature for use is: `cb: Callable, *args, **defaults`, it can receive any sync callable. In the above example, we\nused the `choice` function from the standard library\'s `random` package, and the batch method of `PetFactory`.\n\nYou do not need to use the `Use` field, **you can place callables (including classes) as values for a factory\'s\nattribute** directly, and these will be invoked at build-time. Thus, you could for example re-write the\nabove `PetFactory` like so:\n\n```python\nclass PetFactory(ModelFactory):\n    __model__ = Pet\n\n    name = lambda: choice(["Ralph", "Roxy"])\n    species = lambda: choice(list(Species))\n```\n\n`Use` is merely a semantic abstraction that makes the factory cleaner and simpler to understand.\n\n#### Ignore (field)\n\n`Ignore` is another field exported by this library, and its used - as its name implies - to designate a given attribute\nas ignored:\n\n```python\nfrom typing import TypeVar\n\nfrom odmantic import EmbeddedModel, Model\nfrom pydantic_factories import ModelFactory, Ignore\n\nT = TypeVar("T", Model, EmbeddedModel)\n\n\nclass OdmanticModelFactory(ModelFactory[T]):\n    id = Ignore()\n```\n\nThe above example is basically the extension included in `pydantic-factories` for the\nlibrary [ODMantic](https://github.com/art049/odmantic), which is a pydantic based mongo ODM.\n\nFor ODMantic models, the `id` attribute should not be set by the factory, but rather handled by the odmantic logic\nitself. Thus, the `id` field is marked as ignored.\n\nWhen you ignore an attribute using `Ignore`, it will be completely ignored by the factory - that is, it will not be set\nas a kwarg passed to pydantic at all.\n\n#### Require (field)\n\nThe `Require` field in turn specifies that a particular attribute is a **required kwarg**. That is, if a kwarg with a\nvalue for this particular attribute is not passed when calling `factory.build()`, a `MissingBuildKwargError` will be\nraised.\n\nWhat is the use case for this? For example, lets say we have a document called `Article` which we store in some DB and\nis represented using a non-pydantic model, say, an `elastic-dsl` document. We then need to store in our pydantic object\na reference to an id for this article. This value should not be some mock value, but must rather be an actual id passed\nto the factory. Thus, we can define this attribute as required:\n\n```python\nfrom pydantic import BaseModel\nfrom pydantic_factories import ModelFactory, Require\nfrom uuid import UUID\n\n\nclass ArticleProxy(BaseModel):\n    article_id: UUID\n    ...\n\n\nclass ArticleProxyFactory(ModelFactory):\n    __model__ = ArticleProxy\n\n    article_id = Require()\n```\n\nIf we call `factory.build()` without passing a value for article_id, an error will be raised.\n\n### Persistence\n\n`ModelFactory` has four persistence methods:\n\n- `.create_sync(**kwargs)` - builds and persists a single instance of the factory\'s model synchronously\n- `.create_batch_sync(size: int, **kwargs)` - builds and persists a list of size n instances synchronously\n- `.create_async(**kwargs)` - builds and persists a single instance of the factory\'s model asynchronously\n- `.create_batch_async(size: int, **kwargs)` - builds and persists a list of size n instances asynchronously\n\nTo use these methods, you must first specify a sync and/or async persistence handlers for the factory:\n\n```python\n# persistence.py\nfrom typing import TypeVar, List\n\nfrom pydantic import BaseModel\nfrom pydantic_factories import SyncPersistenceProtocol\n\nT = TypeVar("T", bound=BaseModel)\n\n\nclass SyncPersistenceHandler(SyncPersistenceProtocol[T]):\n    def save(self, data: T) -> T:\n        ...  # do stuff\n\n    def save_many(self, data: List[T]) -> List[T]:\n        ...  # do stuff\n\n\nclass AsyncPersistenceHandler(AsyncPersistenceProtocol[T]):\n    async def save(self, data: T) -> T:\n        ...  # do stuff\n\n    async def save_many(self, data: List[T]) -> List[T]:\n        ...  # do stuff\n```\n\nYou can then specify one or both of these handlers in your factory:\n\n```python\nfrom pydantic_factories import ModelFactory\n\nfrom app.models import Person\nfrom .persistence import AsyncPersistenceHandler, SyncPersistenceHandler\n\n\nclass PersonFactory(ModelFactory):\n    __model__ = Person\n    __sync_persistence__ = SyncPersistenceHandler\n    __async_persistence__ = AsyncPersistenceHandler\n```\n\nOr create your own base factory and reuse it in your various factories:\n\n```python\nfrom pydantic_factories import ModelFactory\n\nfrom app.models import Person\nfrom .persistence import AsyncPersistenceHandler, SyncPersistenceHandler\n\n\nclass BaseModelFactory(ModelFactory):\n    __sync_persistence__ = SyncPersistenceHandler\n    __async_persistence__ = AsyncPersistenceHandler\n\n\nclass PersonFactory(BaseModelFactory):\n    __model__ = Person\n```\n\nWith the persistence handlers in place, you can now use all persistence methods. Please note - you do not need to define\nany or both persistence handlers. If you will only use sync or async persistence, you only need to define the respective\nhandler to use these methods.\n\n## Extensions and Third Party Libraries\n\nAny class that is derived from pydantic\'s `BaseModel` can be used as the `__model__` of a factory. For most 3rd party\nlibraries, e.g. [SQLModel](https://sqlmodel.tiangolo.com/), this library will work as is out of the box.\n\nCurrently, this library also includes the following extensions:\n\n### ODMantic\n\nThis extension includes a class called `OdmanticModelFactory` and it can be imported from `pydantic_factory.extensions`.\nThis class is meant to be used with the `Model` and `EmbeddedModel` classes exported by ODMantic, but it will also work\nwith regular instances of pydantic\'s `BaseModel`.\n\n### Beanie\n\nThis extension includes a class called `BeanieDocumentFactory` as well as an `BeaniePersistenceHandler`. Both of these\ncan be imported from `pydantic_factory.extensions`. The `BeanieDocumentFactory` is meant to be used with the\nBeanie `Document` class, and it includes async persistence build in.\n\n### Ormar\n\nThis extension includes a class called `OrmarModelFactory`. This class is meant to be used with the `Model` class\nexported by ormar.\n\n## Contributing\n\nThis library is open to contributions - in fact we welcome it. [Please see the contribution guide!](CONTRIBUTING.md)\n',
    'author': "Na'aman Hirschfeld",
    'author_email': 'nhirschfeld@gmail.com',
    'maintainer': "Na'aman Hirschfeld",
    'maintainer_email': 'nhirschfeld@gmail.com',
    'url': 'https://github.com/Goldziher/pydantic-factories',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
