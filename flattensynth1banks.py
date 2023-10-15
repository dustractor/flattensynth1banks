import pathlib,shutil,os,argparse

here = pathlib.Path(".").resolve()
_DEFAULT_SOURCE = here / "synth1banksdeep"
_DEFAULT_TARGET = here / "synth1banks"

args = argparse.ArgumentParser()
args.add_argument("--source",type=pathlib.Path,default=_DEFAULT_SOURCE)
args.add_argument("--target",type=pathlib.Path,default=_DEFAULT_TARGET)
ns = args.parse_args()


def main(sourcepath,targetpath):
    patches = list()
    for r,ds,fs in os.walk(sourcepath):
        root = pathlib.Path(r)
        for fp in fs:
            if fp.endswith(".sy1"):
                p = root / fp
                patches.append(p)

    for n,s_patch in enumerate(patches):
        banknum= n // 128
        bankname = "bank_{:03d}".format(banknum)
        patchnum = (n % 128) + 1
        patchname = "{:03d}.sy1".format(patchnum)
        bankdir = targetpath / bankname
        bankdir.mkdir(exist_ok=True)
        t_patch = bankdir / patchname
        shutil.copy(s_patch,t_patch)

if __name__ == "__main__":
    ns.target.mkdir(exist_ok=True)
    main(ns.source,ns.target)

