import subprocess
import helloworld


class TestCLI(object):
    def test_prints_helloworld(self, capfd):
        subprocess.call(['helloworld'])

        out, err = capfd.readouterr()
        assert not err
        assert out.strip() == helloworld.helloworld()
