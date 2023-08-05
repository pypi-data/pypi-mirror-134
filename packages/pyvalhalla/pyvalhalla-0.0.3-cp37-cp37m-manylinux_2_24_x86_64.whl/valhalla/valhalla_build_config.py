#!/usr/bin/env python3
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from distutils.util import strtobool
import json
from typing import List, Union


class Optional:
    def __init__(self, t=None):
        self.type = t


# global default configuration
config = {
    "mjolnir": {
        "max_cache_size": 1000000000,
        "id_table_size": 1300000000,
        "use_lru_mem_cache": False,
        "lru_mem_cache_hard_control": False,
        "use_simple_mem_cache": False,
        "user_agent": Optional(str),
        "tile_url": Optional(str),
        "tile_url_gz": Optional(bool),
        "concurrency": Optional(int),
        "tile_dir": "/data/valhalla",
        "tile_extract": "/data/valhalla/tiles.tar",
        "traffic_extract": "/data/valhalla/traffic.tar",
        "incident_dir": Optional(str),
        "incident_log": Optional(str),
        "shortcut_caching": Optional(bool),
        "admin": "/data/valhalla/admin.sqlite",
        "timezone": "/data/valhalla/tz_world.sqlite",
        "transit_dir": "/data/valhalla/transit",
        "transit_bounding_box": Optional(str),
        "hierarchy": True,
        "shortcuts": True,
        "include_driveways": True,
        "include_bicycle": True,
        "include_pedestrian": True,
        "include_driving": True,
        "import_bike_share_stations": False,
        "global_synchronized_cache": False,
        "max_concurrent_reader_users": 1,
        "reclassify_links": True,
        "default_speeds_config": Optional(str),
        "data_processing": {
            "infer_internal_intersections": True,
            "infer_turn_channels": True,
            "apply_country_overrides": True,
            "use_admin_db": True,
            "use_direction_on_ways": False,
            "allow_alt_name": False,
            "use_urban_tag": False,
            "use_rest_area": False,
            "scan_tar": False,
        },
        "logging": {"type": "std_out", "color": True, "file_name": "path_to_some_file.log"},
    },
    "additional_data": {"elevation": "/data/valhalla/elevation/"},
    "loki": {
        "actions": [
            "locate",
            "route",
            "height",
            "sources_to_targets",
            "optimized_route",
            "isochrone",
            "trace_route",
            "trace_attributes",
            "transit_available",
            "expansion",
            "centroid",
            "status",
        ],
        "use_connectivity": True,
        "service_defaults": {
            "radius": 0,
            "minimum_reachability": 50,
            "search_cutoff": 35000,
            "node_snap_tolerance": 5,
            "street_side_tolerance": 5,
            "street_side_max_distance": 1000,
            "heading_tolerance": 60,
        },
        "logging": {
            "type": "std_out",
            "color": True,
            "file_name": "path_to_some_file.log",
            "long_request": 100.0,
        },
        "service": {"proxy": "ipc:///tmp/loki"},
    },
    "thor": {
        "logging": {
            "type": "std_out",
            "color": True,
            "file_name": "path_to_some_file.log",
            "long_request": 110.0,
        },
        "source_to_target_algorithm": "select_optimal",
        "service": {"proxy": "ipc:///tmp/thor"},
        "max_reserved_labels_count": 1000000,
        "clear_reserved_memory": False,
        "extended_search": False,
    },
    "odin": {
        "logging": {"type": "std_out", "color": True, "file_name": "path_to_some_file.log"},
        "service": {"proxy": "ipc:///tmp/odin"},
        "markup_formatter": {
            "markup_enabled": False,
            "phoneme_format": "<TEXTUAL_STRING> (<span class=<QUOTES>phoneme<QUOTES>>/<VERBAL_STRING>/</span>)",
        },
    },
    "meili": {
        "mode": "auto",
        "customizable": [
            "mode",
            "search_radius",
            "turn_penalty_factor",
            "gps_accuracy",
            "interpolation_distance",
            "sigma_z",
            "beta",
            "max_route_distance_factor",
            "max_route_time_factor",
        ],
        "verbose": False,
        "default": {
            "sigma_z": 4.07,
            "gps_accuracy": 5.0,
            "beta": 3,
            "max_route_distance_factor": 5,
            "max_route_time_factor": 5,
            "max_search_radius": 100,
            "breakage_distance": 2000,
            "interpolation_distance": 10,
            "search_radius": 50,
            "geometry": False,
            "route": True,
            "turn_penalty_factor": 0,
        },
        "auto": {"turn_penalty_factor": 200, "search_radius": 50},
        "pedestrian": {"turn_penalty_factor": 100, "search_radius": 50},
        "bicycle": {"turn_penalty_factor": 140},
        "multimodal": {"turn_penalty_factor": 70},
        "logging": {"type": "std_out", "color": True, "file_name": "path_to_some_file.log"},
        "service": {"proxy": "ipc:///tmp/meili"},
        "grid": {"size": 500, "cache_size": 100240},
    },
    "httpd": {
        "service": {
            "listen": "tcp://*:8002",
            "loopback": "ipc:///tmp/loopback",
            "interrupt": "ipc:///tmp/interrupt",
            "drain_seconds": 28,
            "shutdown_seconds": 1,
        }
    },
    "service_limits": {
        "auto": {
            "max_distance": 5000000.0,
            "max_locations": 20,
            "max_matrix_distance": 400000.0,
            "max_matrix_locations": 50,
        },
        "bus": {
            "max_distance": 5000000.0,
            "max_locations": 50,
            "max_matrix_distance": 400000.0,
            "max_matrix_locations": 50,
        },
        "taxi": {
            "max_distance": 5000000.0,
            "max_locations": 20,
            "max_matrix_distance": 400000.0,
            "max_matrix_locations": 50,
        },
        "pedestrian": {
            "max_distance": 250000.0,
            "max_locations": 50,
            "max_matrix_distance": 200000.0,
            "max_matrix_locations": 50,
            "min_transit_walking_distance": 1,
            "max_transit_walking_distance": 10000,
        },
        "motor_scooter": {
            "max_distance": 500000.0,
            "max_locations": 50,
            "max_matrix_distance": 200000.0,
            "max_matrix_locations": 50,
        },
        "motorcycle": {
            "max_distance": 500000.0,
            "max_locations": 50,
            "max_matrix_distance": 200000.0,
            "max_matrix_locations": 50,
        },
        "bicycle": {
            "max_distance": 500000.0,
            "max_locations": 50,
            "max_matrix_distance": 200000.0,
            "max_matrix_locations": 50,
        },
        "multimodal": {
            "max_distance": 500000.0,
            "max_locations": 50,
            "max_matrix_distance": 0.0,
            "max_matrix_locations": 0,
        },
        "status": {"allow_verbose": False},
        "transit": {
            "max_distance": 500000.0,
            "max_locations": 50,
            "max_matrix_distance": 200000.0,
            "max_matrix_locations": 50,
        },
        "truck": {
            "max_distance": 5000000.0,
            "max_locations": 20,
            "max_matrix_distance": 400000.0,
            "max_matrix_locations": 50,
        },
        "skadi": {"max_shape": 750000, "min_resample": 10.0},
        "isochrone": {
            "max_contours": 4,
            "max_time_contour": 120,
            "max_distance": 25000.0,
            "max_locations": 1,
            "max_distance_contour": 200,
        },
        "trace": {
            "max_distance": 200000.0,
            "max_gps_accuracy": 100.0,
            "max_search_radius": 100.0,
            "max_shape": 16000,
            "max_alternates": 3,
            "max_alternates_shape": 100,
        },
        "bikeshare": {
            "max_distance": 500000.0,
            "max_locations": 50,
            "max_matrix_distance": 200000.0,
            "max_matrix_locations": 50,
        },
        "centroid": {"max_distance": 200000.0, "max_locations": 5},
        "max_exclude_locations": 50,
        "max_reachability": 100,
        "max_radius": 200,
        "max_timedep_distance": 500000,
        "max_alternates": 2,
        "max_exclude_polygons_length": 10000,
    },
    "statsd": {
        "host": Optional(str),
        "port": 8125,
        "prefix": "valhalla",
        "batch_size": Optional(int),
        "tags": Optional(list),
    },
}

help_text = {
    "mjolnir": {
        "max_cache_size": "Number of bytes per thread used to store tile data in memory",
        "id_table_size": "Value controls the initial size of the Id table",
        "use_lru_mem_cache": "Use memory cache with LRU eviction policy",
        "lru_mem_cache_hard_control": "Use hard memory limit control for LRU memory cache (i.e. on every put) - never allow overcommit",
        "use_simple_mem_cache": "Use memory cache within a simple hash map the clears all tiles when overcommitted",
        "user_agent": "User-Agent http header to request single tiles",
        "tile_url": "Http location to read tiles from if they are not found in the tile_dir, e.g.: http://your_valhalla_tile_server_host:8000/some/Optional/path/{tilePath}?some=Optional&query=params. Valhalla will look for the {tilePath} portion of the url and fill this out with a given tile path when it make a request for that tile",
        "tile_url_gz": "Whether or not to request for compressed tiles",
        "concurrency": "How many threads to use in the concurrent parts of tile building",
        "tile_dir": "Location to read/write tiles to/from",
        "tile_extract": "Location to read tiles from tar",
        "traffic_extract": "Location to read traffic from tar",
        "incident_dir": "Location to read incident tiles from",
        "incident_log": "Location to read change events of incident tiles",
        "shortcut_caching": "Precaches the superceded edges of all shortcuts in the graph. Defaults to false",
        "admin": "Location of sqlite file holding admin polygons created with valhalla_build_admins",
        "timezone": "Location of sqlite file holding timezone information created with valhalla_build_timezones",
        "transit_dir": "Location of intermediate transit tiles created with valhalla_build_transit",
        "transit_bounding_box": "Add comma separated bounding box values to only download transit data inside the given bounding box",
        "hierarchy": "bool indicating whether road hierarchy is to be built - default to True",
        "shortcuts": "bool indicating whether shortcuts are to be built - default to True",
        "include_driveways": "bool indicating whether private driveways are included - default to True",
        "include_bicycle": "bool indicating whether cycling only ways are included - default to True",
        "include_pedestrian": "bool indicating whether pedestrian only ways are included - default to True",
        "include_driving": "bool indicating whether driving only ways are included - default to True",
        "import_bike_share_stations": "bool indicating whether importing bike share stations(BSS). Set to True when using multimodal - default to False",
        "global_synchronized_cache": "bool indicating whether global_synchronized_cache is used - default to False",
        "max_concurrent_reader_users": "number of threads in the threadpool which can be used to fetch tiles over the network via curl",
        "reclassify_links": "bool indicating whether or not to reclassify links - reclassifies ramps based on the lowest class connecting road",
        "default_speeds_config": "a path indicating the json config file which graph enhancer will use to set the speeds of edges in the graph based on their geographic location (state/country), density (urban/rural), road class, road use (form of way)",
        "data_processing": {
            "infer_internal_intersections": "bool indicating whether or not to infer internal intersections during the graph enhancer phase or use the internal_intersection key from the pbf",
            "infer_turn_channels": "bool indicating whether or not to infer turn channels during the graph enhancer phase or use the turn_channel key from the pbf",
            "apply_country_overrides": "bool indicating whether or not to apply country overrides during the graph enhancer phase",
            "use_admin_db": "bool indicating whether or not to use the administrative database during the graph enhancer phase or use the admin keys from the pbf that are set on the node",
            "use_direction_on_ways": "bool indicating whether or not to process the direction key on the ways or utilize the guidance relation tags during the parsing phase",
            "allow_alt_name": "bool indicating whether or not to process the alt_name key on the ways during the parsing phase",
            "use_urban_tag": "bool indicating whether or not to use the urban area tag on the ways or to utilize the getDensity function within the graph enhancer phase",
            "use_rest_area": "bool indicating whether or not to use the rest/service area tag on the ways",
            "scan_tar": "bool indicating whether or not to pre-scan the tar ball(s) when loading an extract with an index file, to warm up the OS page cache.",
        },
        "logging": {
            "type": "Type of logger either std_out or file",
            "color": "User colored log level in std_out logger",
            "file_name": "Output log file for the file logger",
        },
    },
    "additional_data": {
        "elevation": "Location of srtmgl1 elevation tiles for using in valhalla_build_tiles"
    },
    "loki": {
        "actions": "Comma separated list of allowable actions for the service, one or more of: locate, route, height, optimized_route, isochrone, trace_route, trace_attributes, transit_available, expansion, centroid, status",
        "use_connectivity": "a boolean value to know whether or not to construct the connectivity maps",
        "service_defaults": {
            "radius": "Default radius to apply to incoming locations should one not be supplied",
            "minimum_reachability": "Default minimum reachability to apply to incoming locations should one not be supplied",
            "search_cutoff": "The cutoff at which we will assume the input is too far away from civilisation to be worth correlating to the nearest graph elements",
            "node_snap_tolerance": "During edge correlation this is the tolerance used to determine whether or not to snap to the intersection rather than along the street, if the snap location is within this distance from the intersection the intersection is used instead",
            "street_side_tolerance": "If your input coordinate is less than this tolerance away from the edge centerline then we set your side of street to none otherwise your side of street will be left or right depending on direction of travel",
            "street_side_max_distance": "The max distance in meters that the input coordinates or display ll can be from the edge centerline for them to be used for determining the side of street. Beyond this distance the side of street is set to none",
            "heading_tolerance": "When a heading is supplied, this is the tolerance around that heading with which we determine whether an edges heading is similar enough to match the supplied heading",
        },
        "logging": {
            "type": "Type of logger either std_out or file",
            "color": "User colored log level in std_out logger",
            "file_name": "Output log file for the file logger",
            "long_request": "Value used in processing to determine whether it took too long",
        },
        "service": {"proxy": "IPC linux domain socket file location"},
    },
    "thor": {
        "logging": {
            "type": "Type of logger either std_out or file",
            "color": "User colored log level in std_out logger",
            "file_name": "Output log file for the file logger",
            "long_request": "Value used in processing to determine whether it took too long",
        },
        "source_to_target_algorithm": "TODO: which matrix algorithm should be used",
        "service": {"proxy": "IPC linux domain socket file location"},
        "max_reserved_labels_count": "Maximum capacity that allowed to keep reserved in path algorithm.",
        "clear_reserved_memory": "If True clean reserved memory in path algorithms",
        "extended_search": "If True and 1 side of the bidirectional search is exhausted, causes the other side to continue if the starting location of that side began on a not_thru or closed edge",
    },
    "odin": {
        "logging": {
            "type": "Type of logger either std_out or file",
            "color": "User colored log level in std_out logger",
            "file_name": "Output log file for the file logger",
        },
        "service": {"proxy": "IPC linux domain socket file location"},
        "markup_formatter": {
            "markup_enabled": "Boolean flag to use markup formatting",
            "phoneme_format": "The phoneme format string that will be used by street names and signs",
        },
    },
    "meili": {
        "mode": "Specify the default transport mode",
        "customizable": "Specify which parameters are allowed to be customized by URL query parameters",
        "verbose": "Control verbose output for debugging",
        "default": {
            "sigma_z": "A non-negative value to specify the GPS accuracy (the variance of the normal distribution) of an incoming GPS sequence. It is also used to weight emission costs of measurements",
            "gps_accuracy": "TODO: ",
            "beta": "A non-negative emprical value to weight the transition cost of two successive candidates",
            "max_route_distance_factor": "A non-negative value used to limit the routing search range which is the distance to next measurement multiplied by this factor",
            "max_route_time_factor": "A non-negative value used to limit the routing search range which is the time to the next measurement multiplied by this factor",
            "breakage_distance": "A non-negative value. If two successive measurements are far than this distance, then connectivity in between will not be considered",
            "max_search_radius": "A non-negative value specifying the maximum radius in meters about a given point to search for candidate edges for routing",
            "interpolation_distance": "If two successive measurements are closer than this distance, then the later one will be interpolated into the matched route",
            "search_radius": "A non-negative value to specify the search radius (in meters) within which to search road candidates for each measurement",
            "geometry": "TODO: ",
            "route": "TODO: ",
            "turn_penalty_factor": "A non-negative value to penalize turns from one road segment to next",
        },
        "auto": {
            "turn_penalty_factor": "A non-negative value to penalize turns from one road segment to next",
            "search_radius": "A non-negative value to specify the search radius (in meters) within which to search road candidates for each measurement",
        },
        "pedestrian": {
            "turn_penalty_factor": "A non-negative value to penalize turns from one road segment to next",
            "search_radius": "A non-negative value to specify the search radius (in meters) within which to search road candidates for each measurement",
        },
        "bicycle": {
            "turn_penalty_factor": "A non-negative value to penalize turns from one road segment to next"
        },
        "multimodal": {
            "turn_penalty_factor": "A non-negative value to penalize turns from one road segment to next"
        },
        "logging": {
            "type": "Type of logger either std_out or file",
            "color": "User colored log level in std_out logger",
            "file_name": "Output log file for the file logger",
        },
        "service": {"proxy": "IPC linux domain socket file location"},
        "grid": {
            "size": "TODO: Resolution of the grid used in finding match candidates",
            "cache_size": "TODO: number of grids to keep in cache",
        },
    },
    "httpd": {
        "service": {
            "listen": "The protocol, host location and port your service will bind to",
            "loopback": "IPC linux domain socket file location used to communicate results back to the client",
            "interrupt": "IPC linux domain socket file location used to cancel work in progress",
            "drain_seconds": "How long to wait for currently running threads to finish before signaling them to shutdown",
            "shutdown_seconds": "How long to wait for currently running threads to quit before exiting the process",
        }
    },
    "service_limits": {
        "auto": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "bus": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "taxi": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "pedestrian": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
            "min_transit_walking_distance": "TODO: minimum distance you must walk to a station",
            "max_transit_walking_distance": "Maximum distance allowed for walking when using transit",
        },
        "motor_scooter": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "motorcycle": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "bicycle": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "multimodal": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "status": {
            "allow_verbose": "Allow verbose output for the /status endpoint, which can be computationally expensive"
        },
        "transit": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "truck": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "skadi": {
            "max_shape": "Maximum number of input shapes",
            "min_resample": "Smalled resampling distance to allow in meters",
        },
        "isochrone": {
            "max_contours": "Maximum number of input contours to allow",
            "max_time_contour": "Maximum time value for any one contour in minutes",
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_distance_contour": "Maximum distance value for any one contour in kilometers",
        },
        "trace": {
            "max_distance": "Maximum input shape distance in meters",
            "max_gps_accuracy": "Maximum input gps accuracy in meters",
            "max_search_radius": "Maximum upper bounds of the search radius in meters",
            "max_shape": "Maximum number of input shape points",
            "max_alternates": "Maximum number of alternate map matching",
            "max_alternates_shape": "Maximum number of input shape points when requesting multiple paths",
        },
        "bikeshare": {
            "max_distance": "Maximum b-line distance between all locations in meters",
            "max_locations": "Maximum number of input locations",
            "max_matrix_distance": "Maximum b-line distance between 2 most distant locations in meters for a matrix",
            "max_matrix_locations": "Maximum number of sources or targets for a matrix",
        },
        "centroid": {
            "max_distance": "Maximum b-line distance between any pair of locations in meters",
            "max_locations": "Maximum number of input locations, 127 is a hard limit and cannot be increased in config",
        },
        "max_exclude_locations": "Maximum number of avoid locations to allow in a request",
        "max_reachability": "Maximum reachability (number of nodes reachable) allowed on any one location",
        "max_radius": "Maximum radius in meters allowed on any one location",
        "max_timedep_distance": "Maximum b-line distance between locations to allow a time-dependent route",
        "max_alternates": "Maximum number of alternate routes to allow in a request",
        "max_exclude_polygons_length": "Maximum total perimeter of all exclude_polygons in meters",
    },
    "statsd": {
        "host": "The statsd host address",
        "port": "The statsd port",
        "prefix": "The statsd prefix to use for each metric",
        "batch_size": "Approximate maximum size in bytes of each batch of stats to send to statsd",
        "tags": "List of tags to include with each metric",
    },
}


def add_leaf_args(
    path: str,
    tree: Union[dict, bool, str, list, Optional],
    leaves_: List[str],
    parser_: ArgumentParser,
    help: dict,
):
    """
    returns a list of leaves of the tree, `\0` separated, stops at non dicts
    while doing so it also adds arguments to the parser
    """
    # if we are at a dict go deeper
    if isinstance(tree, dict):
        for k in tree:
            v = tree[k]
            add_leaf_args("\0".join([path, k]) if len(path) else k, v, leaves_, parser_, help)
    # we've reached a leaf
    else:
        keys = path.split("\0")
        h = help
        for k in keys:
            h = h[k]

        # its either required and is the right type or optional and has a type to use
        # lists are supported as comma separated and bools support a bunch of conventions
        # the rest of the primatives (strings and numbers) parse automatically
        if isinstance(tree, Optional):
            t = tree.type
        elif isinstance(tree, list):
            t = lambda arg: arg.split(",")
        elif isinstance(tree, bool):
            t = lambda arg: bool(strtobool(arg))
        else:
            t = type(tree)

        arg = "--" + path.replace("_", "-").replace("\0", "-")
        parser_.add_argument(arg, type=t, help=h, default=tree)
        leaves_.append(path)


def override_config(args_: dict, leaves_: list, config_: dict):
    """override the defaults given what was passed"""
    for leaf in leaves_:
        keys = leaf.split("\0")
        v = config_
        for k in keys[:-1]:
            v = v[k]
        v[keys[-1]] = args_.get(leaf.replace("\0", "_"))
        if isinstance(v[keys[-1]], type(Optional())):
            del v[keys[-1]]


# set up available program options
leaves = []
parser = ArgumentParser(
    description="Generate valhalla configuration", formatter_class=ArgumentDefaultsHelpFormatter
)
add_leaf_args("", config, leaves, parser, help_text)

# entry point to program
if __name__ == "__main__":
    # TODO: add argument to set base path and use in all other path based values
    args = parser.parse_args()

    # encapsulate to test easier
    override_config(args.__dict__, leaves, config)

    # show the config
    print(json.dumps(config, sort_keys=True, indent=2, separators=(",", ": ")))
