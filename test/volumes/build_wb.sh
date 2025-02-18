#!/bin/sh
# build wb volume from original AmigaOS 3.1.4 disks: Workbench and Modules
#
# build_wb.sh <wb.adf> <modules.adf>

# check adfs
WB_ADF="$1"
MOD_ADF="$2"
if [ "$WB_ADF" == "" -o "$MOD_ADF" == "" ]; then
    echo "Usage: build_wb.sh <wb.adf> <modules.adf>"
    exit 1
fi

# check if 'wb' already exists
WB_OUT="wb"
if [ -d "$WB_OUT" ]; then
    echo "ouput dir '$WB_OUT' already exists!"
    exit 1
fi

# check dirs
WB_DIR="$(basename $1 .adf | sed -e 's/_1_/.1./g')"
MOD_DIR="$(basename $2 .adf | sed -e 's/_1_/.1./g')"
if [ -d "$WB_DIR" ]; then
    echo "WB dir exists: $WB_DIR"
    exit 1
fi
if [ -d "$MOD_DIR" ]; then
    echo "MOD dir exists: $MOD_DIR"
    exit 1
fi

# unpack workbench
echo "unpacking Workbench3.1.4"
../../bin/xdftool $WB_ADF unpack .
mv "$WB_DIR" "$WB_OUT"
rm "${WB_DIR}.blkdev" "${WB_DIR}.bootcode" "${WB_DIR}.xdfmeta"

# unpack modules
echo "unpacking Modules*_3.1.4"
../../bin/xdftool $MOD_ADF unpack .
for DIR in C DEVS L LIBS ; do
    cp -a $MOD_DIR/$DIR/ $WB_OUT/$DIR/
done
rm -rf "$MOD_DIR"
rm "${MOD_DIR}.blkdev" "${MOD_DIR}.xdfmeta"

echo "done"