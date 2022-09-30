import math
from rdkit import Chem
from rdkit.Chem import Draw
#from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem.MolStandardize import rdMolStandardize
#IPythonConsole.drawOptions.comicMode=True
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.info')
import rdkit

smis = ('C[S+2]([O-])([O-])CC','CC[S@](=O)C','C[P+](CC)(N)N','CN=N#N','C=N#N','[N-]=[C+]C','[nH]1c(=[N+](C)C)cccc1','NC=C-C=[N+](C)C','CN(=O)=O','N#N=NC1=CC=CC=C1','[CH+]1C=CC=CC=C1','C1=CC=[C+]C=C1')
ms = []
for smi in smis:
    m = Chem.MolFromSmiles(smi,sanitize=False)
    m.UpdatePropertyCache(strict=False)
    Chem.SanitizeMol(m,sanitizeOps=(Chem.SANITIZE_ALL^Chem.SANITIZE_CLEANUP^Chem.SANITIZE_PROPERTIES))
    cm = rdMolStandardize.Normalize(m)
    ms.extend([m,cm])
    print(Chem.MolToSmiles(cm))
Draw.MolsToGridImage(ms,molsPerRow=4,legends=['input','normalized']*(len(ms)//2))
