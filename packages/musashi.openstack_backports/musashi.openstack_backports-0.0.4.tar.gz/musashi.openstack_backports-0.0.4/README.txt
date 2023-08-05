##### Musashi Icehouse backports

To install set-bootable backport, add the following config to `/etc/cinder/cinder.conf`

```
osapi_volume_extension=musashi.cinder.extensions.volume_actions.Volume_actions_backport
```