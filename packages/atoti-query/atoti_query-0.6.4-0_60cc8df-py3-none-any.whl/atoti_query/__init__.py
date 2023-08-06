"""There are two main ways to query remote atoti sessions (or classic ActivePivot >= 5.7 servers):

* by passing measures and levels to :meth:`atoti_query.query_cube.QueryCube.query`
* by passing an MDX string to :meth:`atoti_query.query_session.QuerySession.query_mdx`
"""

from .auth import Auth as Auth
from .basic_authentication import BasicAuthentication as BasicAuthentication
from .client_certificate import ClientCertificate as ClientCertificate
from .query_cube import QueryCube as QueryCube
from .query_cubes import QueryCubes as QueryCubes
from .query_hierarchies import QueryHierarchies as QueryHierarchies
from .query_hierarchy import QueryHierarchy as QueryHierarchy
from .query_level import QueryLevel as QueryLevel
from .query_levels import QueryLevels as QueryLevels
from .query_measure import QueryMeasure as QueryMeasure
from .query_measures import QueryMeasures as QueryMeasures
from .query_result import QueryResult as QueryResult
from .query_session import QuerySession as QuerySession
from .token_authentication import TokenAuthentication as TokenAuthentication
