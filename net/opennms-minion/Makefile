# $FreeBSD$

PORTNAME=	opennms-minion
PORTVERSION=	${OPENNMS_MAJOR_VERSION}.${OPENNMS_MINOR_VERSION}.${OPENNMS_INC_VERSION}.${OPENNMS_DATE_VERSION}
PORTREVISION=	0
CATEGORIES=	net java

MASTER_SITES=	http://yum.opennms.org/stable/common/opennms/:source1 \
                http://central.maven.org/maven2/:source2
DISTFILES+=	opennms-minion-container-${OPENNMS_PACKAGE_VERSION}.noarch.rpm:source1 \
		opennms-minion-features-core-${OPENNMS_PACKAGE_VERSION}.noarch.rpm:source1 \
		opennms-minion-features-default-${OPENNMS_PACKAGE_VERSION}.noarch.rpm:source1 \
                net/java/dev/jna/jna/4.5.1/jna-4.5.1.jar:source2 \
                net/java/dev/jna/jna-platform/4.5.1/jna-platform-4.5.1.jar:source2
EXTRACT_ONLY=	opennms-minion-container-${OPENNMS_PACKAGE_VERSION}.noarch.rpm \
                opennms-minion-features-core-${OPENNMS_PACKAGE_VERSION}.noarch.rpm \
                opennms-minion-features-default-${OPENNMS_PACKAGE_VERSION}.noarch.rpm

MAINTAINER=	jesse@opennms.org
COMMENT?=	OpenNMS Minion ${OPENNMS_MAJOR_VERSION}

LICENSE=	AGPLv3

EXTRACT_DEPENDS=	rpm2cpio.pl:${PORTSDIR}/archivers/rpm2cpio
RUN_DEPENDS=	javavm:${PORTSDIR}/java/javavmwrapper

OPENNMS_MAJOR_VERSION=  24
OPENNMS_MINOR_VERSION=  0
OPENNMS_INC_VERSION=    0
OPENNMS_DATE_VERSION=	2019.04.26

OPENNMS_PACKAGE_VERSION=	24.0.0-1

USES=           perl5
USE_JAVA=       yes
JAVA_OS=        native
JAVA_VERSION=   1.8
JAVA_VENDOR=    openjdk
JAVA_RUN=       yes

RUN_DEPENDS+=   bash:${PORTSDIR}/shells/bash

USERS=		minion
GROUPS=		minion

MINIONOWN=      minion
MINIONGRP=      minion

INSTPREFIX= 	${PREFIX}/minion

NO_BUILD=	yes

do-install:
		${MKDIR} ${STAGEDIR}${INSTPREFIX}
		(cd ${WRKDIR}/opt/minion && ${COPYTREE_SHARE} . ${STAGEDIR}${INSTPREFIX})
		(cd ${WRKDIR}/opt/minion/bin && ${COPYTREE_BIN} . ${STAGEDIR}${INSTPREFIX}/bin)
		(cp ${DISTDIR}/net/java/dev/jna/jna/4.5.1/jna-4.5.1.jar ${STAGEDIR}${INSTPREFIX}/lib/boot/jna-4.4.0.jar)
		(cp ${DISTDIR}/net/java/dev/jna/jna/4.5.1/jna-4.5.1.jar ${STAGEDIR}${INSTPREFIX}/repositories/default/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar)
		(cp ${DISTDIR}/net/java/dev/jna/jna/4.5.1/jna-4.5.1.jar ${STAGEDIR}${INSTPREFIX}/system/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar)
		(cp ${DISTDIR}/net/java/dev/jna/jna-platform/4.5.1/jna-platform-4.5.1.jar ${STAGEDIR}${INSTPREFIX}/lib/boot/jna-platform-4.4.0.jar)
		(cp ${DISTDIR}/net/java/dev/jna/jna-platform/4.5.1/jna-platform-4.5.1.jar ${STAGEDIR}${INSTPREFIX}/repositories/default/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.jar)
		(cp ${DISTDIR}/net/java/dev/jna/jna-platform/4.5.1/jna-platform-4.5.1.jar ${STAGEDIR}${INSTPREFIX}/system/net/java/dev/jna/jna-platform/4.4.0/jna-platform-4.4.0.jar)
		@(cd ${STAGEDIR}${PREFIX}; ${FIND} -s minion -not -type d) >> ${TMPPLIST}

.include <bsd.port.mk>
