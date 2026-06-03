#!/bin/sh

xsd_path="pynfe/data/XSDs/"
bindings_root_path="pynfe/utils/"

main() {
    # NFSe
    main_xsd_nfse_path="${xsd_path}NFS-e/"
    main_bindings_root_nfse_path="${bindings_root_path}nfse/"

    gera_bindings_diretorio "${main_xsd_nfse_path}Betha/" "${main_bindings_root_nfse_path}betha/"
    ajustes_betha "${main_bindings_root_nfse_path}betha/"

    gera_bindings_diretorio "${main_xsd_nfse_path}Ginfes/" "${main_bindings_root_nfse_path}ginfes/"
    ajustes_ginfes "${main_bindings_root_nfse_path}ginfes/"
}

gera_binding() {
    gb_xsd_nfse_path="$1"
    gb_module="$2"
    gb_bindings_root_nfse_path="$3"

    pyxbgen \
        --schema-location=$gb_xsd_nfse_path \
        --module=$gb_module \
        --binding-root=$gb_bindings_root_nfse_path
}

gera_bindings_diretorio() {
    gbd_xsd_nfse_path="$1"
    gbd_bindings_root_nfse_path="$2"

    for file in $gbd_xsd_nfse_path*.xsd; do
        if [ -f $file ]; then
            filename="${file##*/}"     # retorna apenas o nome do arquivo, sem o caminho - Ex: schema.xsd
            basename="${filename%.*}"  # remove a extensão - Ex: schema

            echo "Gerando: $basename"
            gera_binding "$gbd_xsd_nfse_path${basename}.xsd" $basename $gbd_bindings_root_nfse_path
        fi
    done

    ignorar_lint $gbd_bindings_root_nfse_path
}

ignorar_lint() {
    bindings_root_nfse_path="$1"

    for file in $bindings_root_nfse_path*.py; do
        filename="${file##*/}"     # retorna apenas o nome do arquivo, sem o caminho - Ex: schema.xsd
        if [ -f $file ] && [ $filename != "__init__.py" ]; then
            sed -i '1i# flake8: noqa' $file
        fi
    done
}

ajustes_betha() {
    bindings_root_nfse_path="$1"

    rm "${bindings_root_nfse_path}xmldsig_core_schema20020212.py"

    for file in $bindings_root_nfse_path*.py; do
        filename="${file##*/}"     # retorna apenas o nome do arquivo, sem o caminho - Ex: schema.xsd
        if [ -f $file ] && [ $filename != "__init__.py" ]; then
            sed -i 's/import _dsig/from pynfe.utils.nfse.betha import _dsig/g' $file
        fi
    done
}

ajustes_ginfes() {
    bindings_root_nfse_path="$1"

    rm "${bindings_root_nfse_path}tipos_v03.py"
    rm "${bindings_root_nfse_path}xmldsig_core_schema20020212_v03.py"

    for file in $bindings_root_nfse_path*.py; do
        filename="${file##*/}"     # retorna apenas o nome do arquivo, sem o caminho - Ex: schema.xsd
        if [ -f $file ] && [ $filename != "__init__.py" ]; then
            sed -i 's/import _dsig/from pynfe.utils.nfse.ginfes import _dsig/g' $file
            sed -i 's/import _tipos/from pynfe.utils.nfse.ginfes import _tipos/g' $file
        fi
    done
}

main