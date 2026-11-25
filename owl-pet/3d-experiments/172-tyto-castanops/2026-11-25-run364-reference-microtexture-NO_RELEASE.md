# Run364 — reference-derived triplanar down microtexture (no release)
2026-11-25 Asia/Shanghai. ART_REJECTED / NO_RELEASE. Extra cost $0.

## Preflight
Read main owl-pet AGENTS, README, STATUS (206/251), and #172 v3 review: cream thick mesoptile, developed heart mask, short buried wings, concealed tail, age unknown, science=false. Read Run363 actual record at f39f659af19fb99dba67182a7a687bcc7d63aa10: SDF remesh introduced voxel stripes and 4.75x triangles, rejected. Recovered actual historical Run317 workflow artifact 14795923598; source native SF3D GLB SHA256 c4637faf90b3308123342517b43aabc4b3b197cec8aa62ad80976f173cbe20be. Viewed actual reference juvenile and original browser front/profile. Source atlas visibly has a large streaked rear island. No new neural inference.

## Executed experiment
Instead of further remeshing or a uniform cream repaint, tested whether rear texture can inherit real down microtexture from the original concept chest while preserving the original UV topology, front face and normal map. Rasterized each UV triangle with barycentric weights into a 1024x1024 XYZ/normal atlas; 313118 covered texels. Nearest-coordinate extension up to 5px for texture gutters. Reference JPEG chest crop [285:420,95:270]; high-pass residual subtracting Gaussian sigma=5, clipped to +/-32 RGB units; three mirrored projections in object space with distinct phases and normal-weighted blending. No assertion that the unseen rear feather arrangement is scientifically known. Control and two strengths actually exported as GLB and reopened.
Core executed code:
```python
residual=np.clip(patch-gaussian_filter(patch,(5,5,0)),-32,32)
X,Y,Z=xyz.transpose(2,0,1)
w=np.abs(norm)**3
w/=np.maximum(w.sum(2,keepdims=True),1e-6)
# sample(a,b,off) uses scipy.ndimage.map_coordinates over residual
# coordinates [b*450+off,a*450+off*.7], order=1, mode='reflect'
noise=sample(Z,Y,17)*w[:,:,0,None]+sample(X,Z,47)*w[:,:,1,None]+sample(X,Y,83)*w[:,:,2,None]
# smooth(x) = clip(x,0,1)**2 * (3-2*clip(x,0,1))
body=smooth((Y+.30)/.15)
rear=smooth((Z+.10)/.25)
side=smooth((abs(X)-.12)/.16)*smooth((Z+.21)/.20)
mask=np.maximum(rear,side*.7)*body*(dist<=5)
mod=target+detail*noise+np.clip((base-base.mean(2,keepdims=True))*.12,-7,7)
a=mask[:,:,None]*strength
color=np.clip(base*(1-a)+mod*a,0,255).astype(np.uint8)
# original mesh, UV and normal texture preserved; replace baseColorTexture
```
Soft: strength .65, detail 1.1, target RGB 215,187,157. Full: .94,1.55,224,199,171. Mask >.1 on 181356 texels (including gutters); >.8 on 85438.

| Variant | vertices | triangles | bytes | SHA256 |
|---|---:|---:|---:|---|
| control |16971|27372|1708276|da55e99ef4bb71bbee8dcd55055b40e8dd4c78ee3204cffbe63a157ffe4a6e0b|
| rear-soft |16971|27372|1751152|b70cb2e53b002526cdcafcc389012f438abfb2bddab6e465db3b1a49a099092c|
| rear-full |16971|27372|1785492|29522b5fa5b303944af3fe7dd941cc76a84a1ed44854282d953031e0f067e9fb|

All three actually reopened; normal texture present in all. Rendered twelve actual VTK texture-mapped 3D views (300x300, same orthographic camera 0/45/90/180 degrees; base-color diffuse, not glTF PBR normal map). Inspected 1200x900 contact. Full variant reduces posterior streak texture substantially but does not eliminate underlying horizontal geometry ridges, and transitions around crown remain visibly dark. Side remains an elongated mask-like shape, feet/perch fused, no natural shoulder-wing anatomy or soft volumetric down. Front face retained. Reject all; no new mobile browser/physical phone validation. Do not infer art quality from atlas or geometry integrity.

## Alternative route
Found a CC0 artist-built feathered rigged animated owl at https://blendswap.com/blend/7951 (31.7MB old Blender 2.6x asset, not verified juvenile or suitable). Actual curl HEAD failed DNS (6) Could not resolve host. New local Image To 3D project https://github.com/neko-legends/image-to-3D explicitly targets NVIDIA and does not support CPU generation; torch.cuda.is_available() False, Blender/bpy absent. No new downloadable mesh or paid generation. Prior SF3D/TRIPOSR repairs remain limited. Do not confuse software discovery with execution.

## Evidence
Actual local execution texture.py SHA256 c1fd8c306a6e4c6f445cf61d4b4276693b2b28ac7fcd8ac13e9c6a81e6c1ffdf; report.json 98acd5cca7961ec3ef2bc19c2a36397836c11e0910c35af52a9910e38c3b8759; full contact.jpg b619d7d24e13624eea2b94b49cd48cca065f8f0ed3800a0a63777b75fcfe7825. Full models, atlas, code and renders local to this execution only. Tiny actual-render contact embedded below (120x90, SHA256 38669a1318dd963586dd2b8528ad630fec30abafb3da297eb125e3119b2041b1, evidence only, insufficient for artistic review). No main, production, original concept, or deployment changes.
 
```base64
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAARCABaAHgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDvKzH1NHmKJOkaA8HGS3v9K0JztgkOcYUn9K4LGW3NvDA7ldCcqR06dR6ispOxpFXO3t7lXbZ5qyEjIOMH8qs1zGnyR/aEmjLZL7nLZ5J649gK6eiLugkrMR2CIWY4AGTWL/azy3DASJBCvcjJNaOpHbYyke3864ycMZCOwOcf40Sdgirnb29xHOv7tw5HXFTVg+FQRbTD59isFXeSWHfBPfFb1NO6E1ZkVxOsEe48noB6msk6tMl1GHKeWxwwx2qxrDY8kD1P9Kwb0scHpjvUuWtilHS518brJGrocqwyDTqy/DqTR6UizAgbiUyedp/ya1KtEMzdR1IW0qwx439SfSkttRZnAl2lT/EBjFc5fT+drE7g5XdgfSrkTEJWblZmqimjqqKZEcwofVR/KitDIqa1N5GkXMnfZgfjxXGLMowWJyea7u7to7y1kt5gTHIMHFZVx4bguURHuZiifdGF4/SpkrlRaRhxTO8kcEIJklYKoPf3+lduBgAelZ1npMdpNHL580jRqVUNjAz9BWjRFWQSdzN16cQacST1YCuPS5Dgs+RknA9a7jUbCHUbbyZ9wXO4FTgg1mQ+GYY4TD9qmaLqFKrwfXp1olG44ysWtBiKaeHII8w7hn06Vp1TsrFrQ83c8y4wFkxgfkKuU0rIlu7MTX5hHNACcfKT+tYnmtdXcNtHktI4GfQdzXT6npUGpBPNaRHTIVkODiqMHhi3glWWO7uhIvRgV4/Sk463KUrKxuKoRQqjAAwKUjIIqG2heGMq87znPDOBn9KmqiDzgs9vfTQTjbJGxUitKK5XbjNbmp+HLXU7v7TJLNHKQB8hGOPwqrH4Rt0PN5cn/vkf0qHG5anY2dMl87T4Hzn5cflxRUttbx2ttHBEDsQYGTk0VaIZKSACT0HNc5JrcElyBNu2s21FLYX2H1reumCWszHoEY/pXCqCAwAUhhghu/8AgR2NTJlQVzrLLUIZLgwRgrg7SucgN6Vp1y1ncndFI6hdhzgH35J9zXU0Qd0E1Zkc8ohheQ87RnFcy2pBrhpbku4BwqA4H5VvaqcafJ74H61xzpmQkHoeDn+VKTHFHYaZfx38O+L7gAwQcg1drD8MIywXDNgbnHC9OnJx2zW5VR2JluVb+5NvENv33OB7VgyXkkN1FIXY4OTz1rS1s8wD/eP8qwLtc8k1LepaWh11ncpeWqTxkFX/AEI4NT1n6JZtZ6cqO2S5347LntWh0q0ZswNX1NkvPs0bFQn3vc0tpfPGwYsWX+Jc1gXE32jU5ph0ZyR9KvR/c61k3qapaHXg5AI6Gio7dg1vEw6FR/KitTIpa+7R6JdMoOduOO3I5rj5WktYo3lTardGznn39K9AZQylWAZSMEEZBqhNY6WjDzba3DHoNnP5CplG5UZWObtYJ7m6t4QAqyncWB6KOvHriu0qra21lGfMtoIUYcZVACP61apxVhSdzJ8SXAt9MBP8TgfzrkYDM0HnbC4Y4yOo/D0969BlijmjKSosiHqrDINZ7WWj28hQ29srt/DtyfypONxxlYdoipHYqu9Gkb52CtnFaNV7aztLY77aCKMkYyi4yKsVS0RLd2YHiO4WCa3D8AqcfnWHbzJeajbwlwsZfLk8cCu2nt4blNk8SSr6OoNUhZ6QJFiFvabzwBsHNS463KUtLGirKwypBHsaWooLeG2QpBGsak5IUYGalqiTzq+RtM1Wa2lOQDuRvVT0qzDfxYxursbuzsZjvu7eB26bnUE1BDpWkk5is7Ykc/dzUuKZSlYl0iTzdLgfBwQce4zRVxVCqFUBVAwABgCiqJB22IzHooJrkV1m4EzSKm4FhvIGSoPf6CuovpBDYzyHoqH+VcQq5IKsw6gEfrUTZcEdLZ380l4qyrhWYorHHzAd+O2a2a5G0naLazuWZcYz2x0+grrhyAaIPQJrUhvJTBaySDqBxXIjUHgmd1wZGOMt2rqNWONPkz3IH61xzbWdsc80SYRR1Oh38t9C7SgqyHBRhgqe4rUrF8NReXazNknc4GT1wB0raqo7Ey3KOqTGKJFBxvJz9K5+5uPKmR1PKnNbOsn5oR7E/wAqwbsLx6k4qG9S47HTaRe/b7BJiMPkqw9CP8irtVdOs0sbRIkGCfmc+rHrVo8AmtEZs5fVr9m1VoQflj+XipILkph1OGXmsUyGe9klb7zsTWnHgp0rJmiOqU7lDDuM0VHavvtYm9VFFamZV1uKafSLmO3UtIy8KOp55FchcWtzDHH5STSPxuTyWG36HFd9RScbjUrHI6dp8k97biQT+V9+QNEQMjkDJrrqKKErA3cyvES3Dab/AKNE0rbxuCjJxz2rk7e2uGgOEmWUHLI0TdPrjrXoNGTQ43BSsZeiTR/Zkt0jnVlXczSRlQTn1rUoopoT1MPxF9pVoZIIHlQKQ2wZIP0rCtPtD6hby3Fnc+SjbjiJufTtXc0UrLcfNpYhtrlLqMvGHABwQ6FT+RqaiimI4TV7G6sdWl+zW80lu53qVjJAz1FMgursnC2lwe3+qP8AhXfUZNJxTGpWKmlrKunQCddkmMlT256UVbopiP/Z
```
