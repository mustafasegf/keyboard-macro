{
  description = "python";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/22.05";
    flake-utils.url = "github:numtide/flake-utils";
    pypi-deps-db = {
      url = "github:DavHau/pypi-deps-db/91adfffe522d3571e6549c77695adaa5ef3fecc5";
      flake = true;
    };

    mach-nix = {
      url = "github:DavHau/mach-nix/3.5.0";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.flake-utils.follows = "flake-utils";
      inputs.pypi-deps-db.follows = "pypi-deps-db";
    };
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix, pypi-deps-db }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonEnv = mach-nix.lib."${system}".mkPython {
          ignoreDataOutdated = true;
          python = "python39Full";
          requirements = ''
            evdev
            pynput
          '';
        };
      in
      {
        devShell = pkgs.mkShell {
          nativeBuildInputs = [ ];
          buildInputs = [
            pythonEnv
          ];
        };
      }
    );
}
