from pack import *

wait = xinput()
if wait == "load":
    (user,wahana,pembelian,penggunaan,tiket,refund,kritiksaran,kehilangan) = load()
    nick = login(user)
