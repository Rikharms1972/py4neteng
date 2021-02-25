# See https://napalm.readthedocs.io/en/latest/support/ios.html
# for the explanation of trouble with Cisco IOS banner configurations.
etx_char = chr(3)
with open("Sw1-merge-banner-test.conf", "a") as f:
   f.write("banner motd {}\n".format(etx_char))
   f.write("my banner test\n")
   f.write("{}\n".format(etx_char))

