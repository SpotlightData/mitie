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
      "cflags!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti"],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "/usr/local/include/mitie",
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
