from setux.core.module import Module


class Distro(Module):
    '''Minimum System Requieremnts
    '''
    def do_deploy(self, target, **kw):
        return self.install(target,
            pkg = 'tmux vim',
        )


class FreeBSD(Distro):
    def do_deploy(self, target, **kw):
        return self.install(target,
            pkg = 'sudo bash python',
        )


class Fedora(Distro):
    def do_deploy(self, target, **kw):
        ok = self.install(target,
            pkg = 'langpacks-fr',
        )
        if ok:
            ret, out, err = self.run('localectl set-locale LANG=fr_FR.UTF-8')
            ok = ret == 0
        return ok
