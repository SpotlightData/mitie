{
  "targets": [
    {
      "target_name": "mitie",
      "sources": [
         "src/mitie.cc",
         "src/entity_extractor.cc",
         "src/relation_extractor.cc",
      ],
      "cflags_cc+": [ "-frtti" ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "/root/.linuxbrew/Cellar/mitie/0.4/include/mitie",
        "mitie/dlib/"
      ],
      "link_settings": {
        "libraries": [
          "-lmitie",
          "-lpthread"
        ]
      },
      "conditions": [
        ['OS=="mac"', {
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
            "GCC_ENABLE_CPP_RTTI": "YES",
            "MACOSX_DEPLOYMENT_TARGET": "10.9"
          }
        }]
      ]
    }
  ]
}
