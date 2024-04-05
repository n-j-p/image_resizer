if __name__ == "__main__":
    import sys

    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    quality = [qual for qual in sys.argv[1:] if qual.startswith("-q")]
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
    print('Options:', opts)

    Q = int(quality[0].replace('-q',''))
    print('quality:', Q)
    print('arguments:', args)
    from glob import glob
    filelist = glob(args[0])
    print(filelist)
    from PIL import Image

    for fname in filelist:
        fid=Image.open(fname)
        new_fname = fname.replace('.jpg',
                                  f'%02d.jpg'%Q)
        fid.save(new_fname, quality=Q)
        
        
