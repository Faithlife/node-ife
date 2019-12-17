{
    'conditions': [
        ['OS=="linux"', {
            'targets': [
                {
                    'target_name': 'IFEBinding',
                    'sources': [
                        'addon.cc',
                        'ife.cc',
                        'ife-icmp-support.cc',
                        'ife-sockpacket.cc',
                        'arpcache-proc.cc'
                    ],
                }
            ]
        }],
        ['OS=="solaris"', {
            'targets': [
                {
                    'target_name': 'IFEBinding',
                    'sources': [
                        'addon.cc',
                        'ife.cc',
                        'ife-icmp-support.cc',
                        'ife-dlpi.cc',
                        'arpcache-dlpi.cc'
                    ],
                }
            ]
        }],
        ['1==1', {
            'targets': [ 
                {
                    'target_name': 'IFEStub',
                    'type': 'none'
                }
            ]
        }]
    ]
}
