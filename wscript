# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# def options(opt):
#     pass

# def configure(conf):
#     conf.check_nonfatal(header_name='stdint.h', define_name='HAVE_STDINT_H')

def build(bld):
    module = bld.create_ns3_module('vanetsim', [
                                   'core',
                                   'network',
                                   'mobility',
                                   'wave',
                                   'csma',
                                   'internet',
                                   'point-to-point',
                                   'applications',
                                   'traci',])
                                   
    module.source = [
        'model/beacon-search-net.cc',
        'model/custom-data-tag.cc',
        'model/beacon-rsu-net.cc'
    ]

    headers = bld(features='ns3header')
    headers.module = 'vanetsim'
    headers.source = [
        'model/beacon-search-net.h',
        'model/custom-data-tag.h',
        'model/beacon-rsu-net.h'
    ]

    if bld.env.ENABLE_EXAMPLES:
        bld.recurse('examples')

    # bld.ns3_python_bindings()
