import numpy as np
import pylab as pl
import sciris as sc
import sciris.sc_utils as scu
import sciris.sc_datetime as scd
import sciris.sc_printing as scp

import os
import tempfile

class animation(sc.prettyobj):
    '''
    A class for storing and saving a Matplotlib animation.

    **Examples**::

        anim = sc.animation()
        fig = pl.figure()
        for i in range(50):
            scale = 1/sqrt(i+1)
            x = scale*pl.rand(10)
            y = scale*pl.rand(10)
            label = str(i) if i %% 10 else None
            pl.scatter(x, y, label=label)
            pl.legend()

    '''
    def __init__(self, fig=None, filename=None, dpi=200, fps=10, basename=None, nametemplate=None,
                 imageformat='png', movieformat='mp4', imagefolder=None, usetemp=False, writer=None, verbose=True, **kwargs):
        self.fig = fig
        self.filename = filename
        self.basename = basename
        self.imageformat = imageformat
        self.nametemplate = nametemplate
        self.dpi = dpi
        self.fps = fps
        self.movieformat = movieformat
        self.imagefolder = imagefolder
        self.usetemp = usetemp
        self.writer = writer
        self.verbose = verbose
        self.kwargs = kwargs
        self.filenames = sc.autolist()
        self.frames = sc.autolist()
        self.fig_size = None
        self.fig_dpi = None
        self.anim = None
        self.initialize()
        return


    def initialize(self):

        # Handle basename
        if self.basename is None:
            self.basename = 'animation'

        # Handle folder
        if self.imagefolder is None:
            if self.usetemp:
                self.imagefolder = tempfile.gettempdir()
            else:
                self.imagefolder = os.getcwd()
        self.imagefolder = sc.path(self.imagefolder)

        # Handle name template
        if self.nametemplate is None:
            self.nametemplate = f'{self.basename}_%04d.{self.imageformat}' # ADD name template

        # Handle dpi
        self.dpi = sc.sc_plotting._get_dpi(self.dpi)

        return


    def _getfig(self, fig=None):
        if fig is None:
            if self.fig is not None:
                fig = self.fig
            else:
                try:    fig = self.frames[0][0].get_figure()
                except: fig = pl.gcf()
        return fig


    def _getfilename(self, path=True):
        try:
            name = self.nametemplate % len(self)
        except TypeError as E:
            errormsg = f'Name template "{self.nametemplate}" does not seem valid for inserting current frane number {len(self)} into: should contain the string "%04d" or similar'
            raise TypeError(errormsg) from E
        if path:
            name = self.imagefolder / name
        return name


    def __add__(self, *args, **kwargs):
        return self.addframe(*args, **kwargs)


    def __radd__(self, *args, **kwargs):
        return self.addframe(self, *args, **kwargs)


    def __len__(self):
        return len(self.filenames)


    def addframe(self, fig=None, *args, **kwargs):

        if self.verbose and len(self) == 0: # First frame
            print('Adding frames...')

        # Get the figure, name, and save
        fig = self._getfig(fig)
        filename = self._getfilename()
        fig.savefig(filename, dpi=self.dpi)
        self.filenames += filename

        # Check figure properties
        fig_size = fig.get_size_inches()
        fig_dpi = fig.get_dpi()

        if self.fig_size is None:
            self.fig_size = fig_size
        else:
            if not np.allclose(self.fig_size, fig_size):
                warnmsg = f'Note: current figure size {fig_size} does not match saved {self.fig_size}, unexpected results may occur!'
                print(warnmsg)

        if self.fig_dpi is None:
            self.fig_dpi = fig_dpi
        else:
            if self.fig_dpi != fig_dpi:
                warnmsg = f'Note: current figure DPI {fig_dpi} does not match saved {self.fig_dpi}, unexpected results may occur!'
                print(warnmsg)

        if self.verbose:
            print(f'  Added frame {len(self)}: {self._getfilename(path=False)}')

        return


    def loadframes(self):
        animfig = pl.figure(figsize=self.fig_size, dpi=self.dpi)
        ax = animfig.add_axes([0,0,1,1])
        if self.verbose:
            print('Preprocessing frames...')
        for f,filename in enumerate(self.filenames):
            if self.verbose:
                scp.progressbar(f+1, self.filenames)
            im = pl.imread(filename)
            self.frames += ax.imshow(im)
        pl.close(animfig)
        return


    def __enter__(self, *args, **kwargs):
        return self


    def __exit__(self, *args, **kwargs):
        return self.save()


    def save(self, filename=None, fps=None, dpi=None, anim_args=None, save_args=None,
             writer=None, frames=None, verbose=True, **kwargs):

        import matplotlib.animation as mpl_anim # Sometimes fails if not imported directly

        # Handle dictionary args
        anim_args = sc.mergedicts(anim_args)
        save_args = sc.mergedicts(save_args)

        # Handle filename
        if filename is None:
            if self.filename is None:
                self.filename = f'{self.basename}.{self.movieformat}'
            filename = self.filename

        # Load and sanitize frames
        if frames is None:
            if not len(self.frames):
                self.loadframes()
            frames = self.frames

        for f in range(len(frames)):
            if not scu.isiterable(frames[f]):
                frames[f] = (frames[f],) # This must be either a tuple or a list to work with ArtistAnimation

        # Try to get the figure from the frames, else use the current one
        fig = self._getfig()

        # Set parameters
        if fps    is None: fps    = self.fps
        if dpi    is None: dpi    = self.dpi
        if writer is None: writer = self.writer

        # Optionally print progress
        if verbose:
            T = scd.timer()
            print(f'Saving {len(frames)} frames at {fps} fps and {dpi} dpi to "{filename}" using {writer}...')
            callback = lambda i,n: sc.progressbar(i+1, len(self))
        else:
            callback = None

        # Actually create the animation -- warning, no way to not actually have it render!
        anim = mpl_anim.ArtistAnimation(fig, frames, **anim_args)
        anim.save(filename, writer=writer, fps=fps, dpi=dpi, progress_callback=callback, **save_args)

        if verbose:
            print(f'Done; movie saved to "{filename}"')
            try: # Not essential, so don't try too hard if this doesn't work
                filesize = os.path.getsize(filename)
                if filesize<1e6: print(f'File size: {filesize/1e3:0.0f} KB')
                else:            print(f'File size: {filesize/1e6:0.1f} MB')
            except:
                pass
            T.toc(label='saving movie')

        return



anim = animation()

pl.figure()
pl.seed(1)
repeats = 21
colors = sc.vectocolor(repeats, cmap='turbo')
for i in range(repeats):
    scale = 1/np.sqrt(i+1)
    x = scale*pl.randn(10)
    y = scale*pl.randn(10)
    label = str(i) if not(i%5) else None
    pl.scatter(x, y, c=[colors[i]], label=label)
    pl.title(f'Scale = 1/√{i}')
    pl.legend()
    sc.boxoff('all')
    anim.addframe()

anim.save('dots.mp4')