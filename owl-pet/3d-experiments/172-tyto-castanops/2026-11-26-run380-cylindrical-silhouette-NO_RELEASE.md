# Run380 — measured cylindrical envelope and juvenile silhouette — ART_REJECTED / NO_RELEASE

2026-11-26 Shanghai. Parent fba24505375f6bb02e22cbbbf8e0494af2d15a03. Read main README, AGENTS, STATUS (206/251, 45 remaining) and prior Run379 actual commit. Recovered original neural mesh via Actions artifact 14599833411; SHA256 0e6eedf3ff0b95269555c590c34e996fdc584986d2912f589d817c6ba3b6a02c, 137851 vertices and 275630 triangles, watertight. Viewed 7-axis render and pupil-restored target image. Local scipy/trimesh/VTK/Xvfb tested; Blender absent. No extra paid calls.

## Actual experiment
Avoided increasing ribbon groom density. Reconstructed measured radial envelope of existing Hunyuan3D neural surface in cylindrical coordinates theta=atan2(x,z), r=hypot(x,z), Y vertical. Binned maximum radius into 120 heights x 180 angles; smoothed weighted observed cells by Gaussian sigma=(3,10) with angular wrapping, interpolated radius at each original vertex. On lateral lower body, blend old r toward smoothed radius using smoothstep body mask (-.85,-.49,.32,.64) and flank angle (.32,1.0), k=.65 or .98; front face/toes largely protected. 55 iterations normalized mesh adjacency averaging .5*old+.5*neighbor_mean, local smoothing coefficient .18+.65*body*flank+.35*head*flank. Added modest shoulder/head width and posterior compression. Cream vertex RGB 231,214,187 with small normal-based variation and restricted projected face reference (not claimed as back texture). Exported/reimported two native GLBs. 

Second iteration k=.90 or 1.0: raised rounded crown by .13*smoothstep(.54,.87,Y)*exp(-((X/.38)^2+(Z/.52)^2)), stronger lower posterior compression .38*(1-smoothstep(-.82,-.22,Y)), additional front breast smooth/raised lower body. Original Z span 1.7174; round Z span 1.4322 (16.6% reduction); original upper Y .98785, round 1.10759. Each GLB retained 275630 triangles and vertex colors; watertight at export. Four actual 340x340 VTK offscreen views each, front +Z, +Y up, angles 0/45/90/180; 16 renders total. Both sheets visually inspected.

## Art assessment
V1 shoulder ridge still visible, flattened crown, long rear silhouette. V2 reduces tail projection and rounds crown, but flank remains adult-like with folded-wing groove, back bulge unnatural, face pigment looks printed, eyes too flat, exposed feet and stiff surface lack thick juvenile mesoptile. All four reject. No mobile WebGL run because art gate failed. No fresh neural inference or scientifically approved age claim. Next: focus on actual branching down and reference-driven face geometry, not further global compression.

## Evidence
Actual V2 round four views, miniature JPEG, 200x50, 1425 bytes. Full-resolution sheet and native GLBs/scripts locally generated only; remote report includes hashes and thumbnail encoding, not full mesh binaries.
SHA256 thumbnail 5cee658a8f4d58a3d10557f69b4e1025e028de3dad42216f1003e27bbc20dcda
moderate GLB 202849fc4fbf31d50ff66c3eb8a9563712e5adc07904b0d0b14dc77dc54633f2
strong GLB 4e1e5569abef4edb94120c1ec86b565bb87202c7370d0c1c415ae49536bc2826
round GLB d9a80be980f500dd8d3d68ba869469052e5d472e0e6b75fd2387344bcfed9d15
round_deep GLB dc7b3caf693fd664374ab23f878099d6558fbc85f3f08ce6a019e5d2febb0ec1
V1 sheet 1736fdef6be436cea652d5f7554586835d713e80bb43e3e9c0559d7bd2f59bb5
V2 sheet a18874305eb5f2b8adc1d37d1aa2058abad86952c68721d7a6bc764b02f4e632
V1 sculpt b1a71c585b7093096cdc1b7112321da8fc2f6c4169488acd48ab98bb430063e8
V2 sculpt 67075a45b392ba50e7c22e970c60e34cf005be04be4068538b1cbd656d5c99a7
V1 render 6020cc686e741811d09702ed4dad97dd93fb660b15c5f9b6e82aa61bebf47ded
V2 render 53b7897bf321622744e41f333093caafacf904ff8dc1ca35f84c6e8d3406547c

Base64 JPEG:
```
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDABQODxIPDRQSEBIXFRQYHjIhHhwcHj0sLiQySUBMS0dARkVQWnNiUFVtVkVGZIhlbXd7gYKBTmCNl4x9lnN+gXz/2wBDARUXFx4aHjshITt8U0ZTfHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHz/wAARCAAyAMgDASIAAhEBAxEB/8QAGgAAAwEBAQEAAAAAAAAAAAAAAAMEBQECBv/EADIQAAICAQMCAwYEBwEAAAAAAAECAAMRBBIhMUETIlEFFDJCYXEjNIGRJFJykqGxweH/xAAYAQEBAQEBAAAAAAAAAAAAAAADAAIBBP/EABsRAQEBAQEBAQEAAAAAAAAAAAABAhESMUEh/9oADAMBAAIRAxEAPwD6acZgqlmOABkmdmf7UsY1mms4JGWx/idt5HJOvL+0fEYrU6oB+/8A5PHvr08m4MPRpnWPqNE1TVUo+n43GU6trhbTRpK0w5LWE9hC9UvmNjT6hNQm5Oo6j0jZjaL+F1OB8BO0gdBNmJm9g7OUROp1VWmXNjcnovcx0wNYbH9qurANU2U57HHEtXik6rOua5wotVM9FU8/vHJfbTg2HfX3PcTHTx31FhuqVUrbCEfSbi1FqT6EQ/Vb8xUDkZHIhJdE52tS3VOn2lUWXoxE6nVVaZVNh5Y4UdyY6Y/tcsdfpBtBrGdxzyCen+pW8ik7VXjai8+XCL6Dr+8PGuoINjbkzyCOZVp021DHeK1KZQ5HML1ek5FIIIBHIMJNoLN1Gw9azt/TtKYsGIQhOuF33LSuSMk9FHeJXx7eWs2D0WKJ941TP8q+VZagwIWtEkTeNbQ34n4ieuORKlYMoZTkEZBirkyInRWFWahu3K/adzr8rmoshCERhwkKCT0HMz662vRnPxMcy3U/l7f6TE6XIrBHEPbeU66ParV2c1sOuOk7VpRSPK3i2YwMekvBI5BxDLH5h+kNtmWUNTWxY5Y8kiaikMoYdCMxFygoQeYaEk6cA/KSsTFY0omNZWG19zkjIfIB79pszLuBr1744zzO7+OZ+mV6IuqgHCjkk9zNBU2JiIqsLAZMoD9j3hERWnwbls7A4b7SyJ1VYZTDSOX0yE9Rwf0iYv4xqHTK19W7XKzHoBjiasm11Jsp3J8dfIHrNanY5Lyn0HyAT1aoZZFobtygEy4jIgkZiN7tqwfkfyt/wzSkGtrBUyrS2G3TVuepHMXFY1DZxjtUk9AMzsRrSRpyB8xAmqyRpB5BLADiJoXyiUAQCvDAyS8bGFg6qcy4iSakAKZRKgQQCOh5hPGn/L1/0iE9Anp13oy/zAiRaSw7dh+JeCJfI79M3j+LWSOhIA6zGp13NPLAgg8EdoBgAMck9pLebnZX8NsjgrgztBuQs+xs9ACIfK313UXbFJ/xH6Ss1UKG+I8n9YirSE3eJacgHIXHeWxMzjOqJFr6iGS9edvlYfSWxV5YoyqpP/Zq/GYlUhWVlPlbj7GVK+5eQeYq6s3LnZsYjmeHez3fwxW4KjjymDyk6bYxCnJ4nrSrt06fUZ/eSIl93lZGUHqW4mgAAAB0E3icZ1XYQgeIjDMuT3bU8cI/Kn09RLqrTgA95xiWsXKEqB0xJ7UuRt1FTbO65/1Cs7f4SUv2gxCkiX0oK6UVegUTOtF2pAQUOpPBLDAE01G1QPQYmsRzTsVqUL0kDqORGwm2SKCHUEGUBfrJXVqX3VozK3JAHSexqGHWp/7YFzYSU4r9ZJqh5cDkngRp1BPSqz+2eUDWXhnRlCjIyO8pKrT0XYir6DEJ2EcYhCEnBCEJIQhCSEIQkhCEJIQhCSEIQkhCEJIQhCSEIQkhCEJIQhCSEIQkn//Z
```

No main, concept, deployment or production workflow changes. ART_REJECTED / NO_RELEASE.
