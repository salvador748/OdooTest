# Git - QPS 

### help 
* ```git help paramentro [config, branch]```

### config 
* Configuraciones generales 
    * ```git config --global user.name ""```
    * ```git config --global user.email ""```
    * ```git config --list ```
    * ubicación del archivo ```~/.gitconfig```

### .gitignore
* Archivo donde se define la omision de carpetas/archivos


## remote 
* Agregar repo remoto 
    * ```git remote add [nombre/alias del remoto] [url]```
    

### branch
* Creación de ramas
    * ```git checkout -b staging ```
    * ```git branch develop```
```
local 
    \ -- master  --> producción 
     \  -- staging  -> pre-producciín  
      \  -- develop  -> Desarrollo            
```

### merge
* Unir dos ramas
    * ```git merge origin/master```
```
local 
    \-- master --- -> master local + remote
                 /
remote          /
    \-- master /
```

### add
* Preparar para incluir en el siguiente commit 
    * ```git add  [nombre archivo]```
    * ```git add -A ```

### commit 
* Confirmar cambios para subir 
    * ```git commit -m [mensaje corto]```
    * ```git commit ```
    
### rm 
* Eliminar archivos
    * ```git rm [nombre archivo]```

### reset 
* Eliminar commits 
    * ```git reset HEAD [nombre archivo] ```
    






