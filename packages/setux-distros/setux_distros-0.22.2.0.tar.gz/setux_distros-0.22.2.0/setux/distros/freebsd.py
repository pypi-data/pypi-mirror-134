from setux.core.distro import Distro


class FreeBSD(Distro):
    Package = 'pkg'
    Service = 'Service'

    @classmethod
    def release_infos(cls, target):
        ret, out, err = target.run('uname -s', report='quiet')
        distro = out[0]
        if distro=='FreeBSD':
            ret, out, err = target.run('uname -r', report='quiet')
            ver = out[0].split('.')[0]
            return dict(
                ID         = distro,
                VERSION_ID = ver,
            )

