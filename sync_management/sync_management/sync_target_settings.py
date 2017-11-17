# -*- coding: utf-8 -*-
# Copyright (c) 2015, erpx and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

import json

class SyncTargetSettings(Document):
	pass
@frappe.whitelist()
def switch_name_doc(self, method):
	if self.is_sync == 0:
		return
	frappe.db.sql(""" UPDATE `tab{} Item` ol JOIN `tab{} Item` nu USING (NAME) 
		SET nu.name = ol.tampungan_awal, nu.tampungan_awal = ol.name WHERE ol.parent = "{}" """.format(self.doctype, self.doctype, self.name))
	frappe.db.commit()
	frappe.db.close()

@frappe.whitelist()
def sync_autoname (self, method):
	if self.is_sync == 0:
		return

	check_nama = frappe.get_all('Custom Sync Naming', filters={'name': self.doctype}, fields=['name'])

	if not check_nama:
		frappe.throw("Silahkan mengisi series untuk dokumen {} di sync ini di Custom Sync Naming.".format(self.doctype))
	else:	
		nama_series = frappe.get_doc("Custom Sync Naming", self.doctype)
		from frappe.model.naming import make_autoname
		self.name = make_autoname(nama_series.sync_naming_series)