import maya.cmds as cmds

follicleShape = 'follicleShape16'
geometryShapeNode = 'geo_Lids_00_nShape'
group = 'R_Lid_Ctl_03_Grp'
groupAfter = 'R_Lid_Ctl_02_Grp'

#Desconecta el nodo ClosestclosestPointOnMesh1
cmds.disconnectAttr(groupAfter +'.translate', 'closestPointOnMesh1.inPosition')

# Conecta el output Translate del grupo del control al input In Position del nodo ClosestPointOnMesh
cmds.connectAttr(group +'.translate', 'closestPointOnMesh1.inPosition')

# Crea un folículo
follicleNode = cmds.createNode('follicle', n=follicleShape)

# Conecta el output del nodo shape del folículo Out Translate al Input Translate del nodo objeto del folículo
cmds.connectAttr(follicleShape + '.outTranslate', 'follicle16.translate')

# Conecta el output Out Mesh del nodo shape de la geometría al Input InputMesh del nodo shape del folículo
cmds.connectAttr(geometryShapeNode + '.outMesh', follicleShape + '.inputMesh')

# Conecta el Input Parameter U del nodo ClosestPointOnMesh al input Parameter U del nodo shape del folículo
cmds.connectAttr('closestPointOnMesh1.parameterU', follicleShape + '.parameterU')

# Conecta el Input Parameter V del nodo ClosestPointOnMesh al input Parameter V del nodo shape del folículo
cmds.connectAttr('closestPointOnMesh1.parameterV', follicleShape + '.parameterV')

# Desconecta el Input Parameter V del nodo ClosestPointOnMesh del input Parameter V del nodo shape del folículo
cmds.disconnectAttr('closestPointOnMesh1.parameterV', follicleShape + '.parameterV')

# Desconecta el Input Parameter U del nodo ClosestPointOnMesh del input Parameter U del nodo shape del folículo
cmds.disconnectAttr('closestPointOnMesh1.parameterU', follicleShape + '.parameterU')
