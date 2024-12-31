# Generated with JReleaser 1.16.0-SNAPSHOT at 2024-12-31T11:03:40.173959401Z
Name:      jreleaser
Version:   1.16.0
Release:   1%{?dist}
Summary:   Release projects quickly and easily with JReleaser

License:   Apache-2.0
URL:       https://jreleaser.org
Source0:   https://github.com/jreleaser/jreleaser/releases/download/v1.16.0/jreleaser-1.16.0.tar

BuildArch: noarch
Requires:  java

%description
JReleaser is a release automation tool. Its goal is to simplify creating releases and
publishing artifacts to multiple package managers while providing customizable options.

JReleaser takes inputs from popular builds tools (Ant, Maven, Gradle) such as JAR files,
binary distributions (.zip, .tar), JLink images, or any other file that you’d like to
publish as a Git release on popular Git services such as GitHub, GitLab, or Gitea.
Distribution files may additionally be published to be consumed by popular package managers
such as Homebrew, Chocolatey, Snapcraft, or get ready to be launched via JBang. Releases
may be announced in a variety of channels such as Twitter, Zulip, SDKMAN!, and more.


%prep
%setup -q -n jreleaser-1.16.0

%install
mkdir -p %{buildroot}%{_bindir}
%define _appdir %{buildroot}%{_datadir}/%{name}
mkdir -p %{_appdir}/bin

cat > %{buildroot}%{_bindir}/jreleaser <<-EOF
#!/bin/sh
%{_datadir}/%{name}/bin/jreleaser "$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/jreleaser

mkdir -p %{_appdir}/SWIDTAG
mkdir -p %{_appdir}/lib
mkdir -p %{_appdir}/licenses
install -p -m 755 bin/jreleaser %{_appdir}/bin/jreleaser
install -p -m 644 LICENSE %{_appdir}/LICENSE
install -p -m 644 NOTICE %{_appdir}/NOTICE
install -p -m 644 SWIDTAG/swid-tag.xml %{_appdir}/SWIDTAG/swid-tag.xml
install -p -m 644 lib/JavaEWAH-1.2.3.jar %{_appdir}/lib/JavaEWAH-1.2.3.jar
install -p -m 644 lib/annotations-2.29.39.jar %{_appdir}/lib/annotations-2.29.39.jar
install -p -m 644 lib/apache-client-2.29.39.jar %{_appdir}/lib/apache-client-2.29.39.jar
install -p -m 644 lib/arns-2.29.39.jar %{_appdir}/lib/arns-2.29.39.jar
install -p -m 644 lib/asn-one-0.6.0.jar %{_appdir}/lib/asn-one-0.6.0.jar
install -p -m 644 lib/auth-2.29.39.jar %{_appdir}/lib/auth-2.29.39.jar
install -p -m 644 lib/autolink-0.10.1.jar %{_appdir}/lib/autolink-0.10.1.jar
install -p -m 644 lib/aws-core-2.29.39.jar %{_appdir}/lib/aws-core-2.29.39.jar
install -p -m 644 lib/aws-query-protocol-2.29.39.jar %{_appdir}/lib/aws-query-protocol-2.29.39.jar
install -p -m 644 lib/aws-xml-protocol-2.29.39.jar %{_appdir}/lib/aws-xml-protocol-2.29.39.jar
install -p -m 644 lib/bcpg-jdk18on-1.79.jar %{_appdir}/lib/bcpg-jdk18on-1.79.jar
install -p -m 644 lib/bcpkix-jdk18on-1.79.jar %{_appdir}/lib/bcpkix-jdk18on-1.79.jar
install -p -m 644 lib/bcprov-jdk18on-1.79.jar %{_appdir}/lib/bcprov-jdk18on-1.79.jar
install -p -m 644 lib/bcutil-jdk18on-1.79.jar %{_appdir}/lib/bcutil-jdk18on-1.79.jar
install -p -m 644 lib/checksums-2.29.39.jar %{_appdir}/lib/checksums-2.29.39.jar
install -p -m 644 lib/checksums-spi-2.29.39.jar %{_appdir}/lib/checksums-spi-2.29.39.jar
install -p -m 644 lib/classmate-1.7.0.jar %{_appdir}/lib/classmate-1.7.0.jar
install -p -m 644 lib/commonmark-0.21.0.jar %{_appdir}/lib/commonmark-0.21.0.jar
install -p -m 644 lib/commonmark-ext-autolink-0.21.0.jar %{_appdir}/lib/commonmark-ext-autolink-0.21.0.jar
install -p -m 644 lib/commons-codec-1.17.1.jar %{_appdir}/lib/commons-codec-1.17.1.jar
install -p -m 644 lib/commons-compress-1.27.1.jar %{_appdir}/lib/commons-compress-1.27.1.jar
install -p -m 644 lib/commons-io-2.18.0.jar %{_appdir}/lib/commons-io-2.18.0.jar
install -p -m 644 lib/commons-jexl3-3.4.0.jar %{_appdir}/lib/commons-jexl3-3.4.0.jar
install -p -m 644 lib/commons-lang3-3.17.0.jar %{_appdir}/lib/commons-lang3-3.17.0.jar
install -p -m 644 lib/commons-net-3.11.1.jar %{_appdir}/lib/commons-net-3.11.1.jar
install -p -m 644 lib/commons-text-1.13.0.jar %{_appdir}/lib/commons-text-1.13.0.jar
install -p -m 644 lib/compiler-0.9.14.jar %{_appdir}/lib/compiler-0.9.14.jar
install -p -m 644 lib/crt-core-2.29.39.jar %{_appdir}/lib/crt-core-2.29.39.jar
install -p -m 644 lib/eddsa-0.3.0.jar %{_appdir}/lib/eddsa-0.3.0.jar
install -p -m 644 lib/endpoints-spi-2.29.39.jar %{_appdir}/lib/endpoints-spi-2.29.39.jar
install -p -m 644 lib/eventstream-1.0.1.jar %{_appdir}/lib/eventstream-1.0.1.jar
install -p -m 644 lib/failsafe-3.3.2.jar %{_appdir}/lib/failsafe-3.3.2.jar
install -p -m 644 lib/feign-core-13.5.jar %{_appdir}/lib/feign-core-13.5.jar
install -p -m 644 lib/feign-form-3.8.0.jar %{_appdir}/lib/feign-form-3.8.0.jar
install -p -m 644 lib/feign-httpclient-13.5.jar %{_appdir}/lib/feign-httpclient-13.5.jar
install -p -m 644 lib/feign-jackson-13.5.jar %{_appdir}/lib/feign-jackson-13.5.jar
install -p -m 644 lib/http-auth-2.29.39.jar %{_appdir}/lib/http-auth-2.29.39.jar
install -p -m 644 lib/http-auth-aws-2.29.39.jar %{_appdir}/lib/http-auth-aws-2.29.39.jar
install -p -m 644 lib/http-auth-aws-eventstream-2.29.39.jar %{_appdir}/lib/http-auth-aws-eventstream-2.29.39.jar
install -p -m 644 lib/http-auth-spi-2.29.39.jar %{_appdir}/lib/http-auth-spi-2.29.39.jar
install -p -m 644 lib/http-client-spi-2.29.39.jar %{_appdir}/lib/http-client-spi-2.29.39.jar
install -p -m 644 lib/httpclient-4.5.14.jar %{_appdir}/lib/httpclient-4.5.14.jar
install -p -m 644 lib/httpcore-4.4.16.jar %{_appdir}/lib/httpcore-4.4.16.jar
install -p -m 644 lib/identity-spi-2.29.39.jar %{_appdir}/lib/identity-spi-2.29.39.jar
install -p -m 644 lib/jackson-annotations-2.18.2.jar %{_appdir}/lib/jackson-annotations-2.18.2.jar
install -p -m 644 lib/jackson-core-2.18.2.jar %{_appdir}/lib/jackson-core-2.18.2.jar
install -p -m 644 lib/jackson-databind-2.18.2.jar %{_appdir}/lib/jackson-databind-2.18.2.jar
install -p -m 644 lib/jackson-dataformat-toml-2.18.2.jar %{_appdir}/lib/jackson-dataformat-toml-2.18.2.jar
install -p -m 644 lib/jackson-dataformat-xml-2.18.2.jar %{_appdir}/lib/jackson-dataformat-xml-2.18.2.jar
install -p -m 644 lib/jackson-dataformat-yaml-2.18.2.jar %{_appdir}/lib/jackson-dataformat-yaml-2.18.2.jar
install -p -m 644 lib/jackson-datatype-jsr310-2.18.2.jar %{_appdir}/lib/jackson-datatype-jsr310-2.18.2.jar
install -p -m 644 lib/jakarta.activation-2.0.1.jar %{_appdir}/lib/jakarta.activation-2.0.1.jar
install -p -m 644 lib/jakarta.mail-2.0.1.jar %{_appdir}/lib/jakarta.mail-2.0.1.jar
install -p -m 644 lib/jcl-over-slf4j-2.0.16.jar %{_appdir}/lib/jcl-over-slf4j-2.0.16.jar
install -p -m 644 lib/jreleaser-1.16.0.jar %{_appdir}/lib/jreleaser-1.16.0.jar
install -p -m 644 lib/jreleaser-artifactory-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-artifactory-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-azure-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-azure-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-bluesky-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-bluesky-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-codeberg-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-codeberg-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-command-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-command-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-config-json-1.16.0.jar %{_appdir}/lib/jreleaser-config-json-1.16.0.jar
install -p -m 644 lib/jreleaser-config-toml-1.16.0.jar %{_appdir}/lib/jreleaser-config-toml-1.16.0.jar
install -p -m 644 lib/jreleaser-config-yaml-1.16.0.jar %{_appdir}/lib/jreleaser-config-yaml-1.16.0.jar
install -p -m 644 lib/jreleaser-discord-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-discord-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-discourse-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-discourse-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-engine-1.16.0.jar %{_appdir}/lib/jreleaser-engine-1.16.0.jar
install -p -m 644 lib/jreleaser-ftp-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-ftp-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-genericgit-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-genericgit-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-git-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-git-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-gitea-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-gitea-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-github-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-github-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-gitlab-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-gitlab-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-gitter-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-gitter-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-google-chat-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-google-chat-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-http-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-http-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-java-sdk-commons-1.16.0.jar %{_appdir}/lib/jreleaser-java-sdk-commons-1.16.0.jar
install -p -m 644 lib/jreleaser-linkedin-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-linkedin-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-logger-api-1.16.0.jar %{_appdir}/lib/jreleaser-logger-api-1.16.0.jar
install -p -m 644 lib/jreleaser-mastodon-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-mastodon-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-mattermost-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-mattermost-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-mavencentral-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-mavencentral-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-model-api-1.16.0.jar %{_appdir}/lib/jreleaser-model-api-1.16.0.jar
install -p -m 644 lib/jreleaser-model-impl-1.16.0.jar %{_appdir}/lib/jreleaser-model-impl-1.16.0.jar
install -p -m 644 lib/jreleaser-nexus2-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-nexus2-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-opencollective-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-opencollective-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-resource-bundle-1.16.0.jar %{_appdir}/lib/jreleaser-resource-bundle-1.16.0.jar
install -p -m 644 lib/jreleaser-s3-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-s3-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-sdkman-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-sdkman-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-signing-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-signing-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-slack-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-slack-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-smtp-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-smtp-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-ssh-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-ssh-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-teams-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-teams-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-telegram-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-telegram-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-templates-1.16.0.jar %{_appdir}/lib/jreleaser-templates-1.16.0.jar
install -p -m 644 lib/jreleaser-tool-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-tool-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-twitter-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-twitter-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-utils-1.16.0.jar %{_appdir}/lib/jreleaser-utils-1.16.0.jar
install -p -m 644 lib/jreleaser-webhooks-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-webhooks-java-sdk-1.16.0.jar
install -p -m 644 lib/jreleaser-zulip-java-sdk-1.16.0.jar %{_appdir}/lib/jreleaser-zulip-java-sdk-1.16.0.jar
install -p -m 644 lib/json-utils-2.29.39.jar %{_appdir}/lib/json-utils-2.29.39.jar
install -p -m 644 lib/jsonschema-generator-4.36.0.jar %{_appdir}/lib/jsonschema-generator-4.36.0.jar
install -p -m 644 lib/jsonschema-module-jackson-4.36.0.jar %{_appdir}/lib/jsonschema-module-jackson-4.36.0.jar
install -p -m 644 lib/metrics-spi-2.29.39.jar %{_appdir}/lib/metrics-spi-2.29.39.jar
install -p -m 644 lib/org.eclipse.jgit-5.13.3.202401111512-r.jar %{_appdir}/lib/org.eclipse.jgit-5.13.3.202401111512-r.jar
install -p -m 644 lib/picocli-4.7.6.jar %{_appdir}/lib/picocli-4.7.6.jar
install -p -m 644 lib/profiles-2.29.39.jar %{_appdir}/lib/profiles-2.29.39.jar
install -p -m 644 lib/protocol-core-2.29.39.jar %{_appdir}/lib/protocol-core-2.29.39.jar
install -p -m 644 lib/reactive-streams-1.0.4.jar %{_appdir}/lib/reactive-streams-1.0.4.jar
install -p -m 644 lib/regions-2.29.39.jar %{_appdir}/lib/regions-2.29.39.jar
install -p -m 644 lib/retries-2.29.39.jar %{_appdir}/lib/retries-2.29.39.jar
install -p -m 644 lib/retries-spi-2.29.39.jar %{_appdir}/lib/retries-spi-2.29.39.jar
install -p -m 644 lib/s3-2.29.39.jar %{_appdir}/lib/s3-2.29.39.jar
install -p -m 644 lib/sdk-core-2.29.39.jar %{_appdir}/lib/sdk-core-2.29.39.jar
install -p -m 644 lib/slf4j-api-2.0.16.jar %{_appdir}/lib/slf4j-api-2.0.16.jar
install -p -m 644 lib/slf4j-simple-2.0.16.jar %{_appdir}/lib/slf4j-simple-2.0.16.jar
install -p -m 644 lib/snakeyaml-2.3.jar %{_appdir}/lib/snakeyaml-2.3.jar
install -p -m 644 lib/sshj-0.39.0.jar %{_appdir}/lib/sshj-0.39.0.jar
install -p -m 644 lib/stax2-api-4.2.2.jar %{_appdir}/lib/stax2-api-4.2.2.jar
install -p -m 644 lib/third-party-jackson-core-2.29.39.jar %{_appdir}/lib/third-party-jackson-core-2.29.39.jar
install -p -m 644 lib/tika-core-2.9.2.jar %{_appdir}/lib/tika-core-2.9.2.jar
install -p -m 644 lib/twitter4j-core-4.1.2.jar %{_appdir}/lib/twitter4j-core-4.1.2.jar
install -p -m 644 lib/utils-2.29.39.jar %{_appdir}/lib/utils-2.29.39.jar
install -p -m 644 lib/woodstox-core-7.1.0.jar %{_appdir}/lib/woodstox-core-7.1.0.jar
install -p -m 644 lib/xz-1.10.jar %{_appdir}/lib/xz-1.10.jar
install -p -m 644 lib/yamllint-1.6.1.jar %{_appdir}/lib/yamllint-1.6.1.jar
install -p -m 644 lib/zstd-jni-1.5.6-8.jar %{_appdir}/lib/zstd-jni-1.5.6-8.jar
install -p -m 644 licenses/LICENSE-BSD-2-Clause %{_appdir}/licenses/LICENSE-BSD-2-Clause
install -p -m 644 licenses/LICENSE-BSD-2-Clause-FreeBSD %{_appdir}/licenses/LICENSE-BSD-2-Clause-FreeBSD
install -p -m 644 licenses/LICENSE-Bouncy-Castle %{_appdir}/licenses/LICENSE-Bouncy-Castle
install -p -m 644 licenses/LICENSE-CC0 %{_appdir}/licenses/LICENSE-CC0
install -p -m 644 licenses/LICENSE-EDL-1.0 %{_appdir}/licenses/LICENSE-EDL-1.0
install -p -m 644 licenses/LICENSE-MIT %{_appdir}/licenses/LICENSE-MIT
install -p -m 644 licenses/LICENSE-jzlib %{_appdir}/licenses/LICENSE-jzlib

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/bin/jreleaser
%{_datadir}/%{name}/LICENSE
%{_datadir}/%{name}/NOTICE
%{_datadir}/%{name}/SWIDTAG/swid-tag.xml
%{_datadir}/%{name}/lib/JavaEWAH-1.2.3.jar
%{_datadir}/%{name}/lib/annotations-2.29.39.jar
%{_datadir}/%{name}/lib/apache-client-2.29.39.jar
%{_datadir}/%{name}/lib/arns-2.29.39.jar
%{_datadir}/%{name}/lib/asn-one-0.6.0.jar
%{_datadir}/%{name}/lib/auth-2.29.39.jar
%{_datadir}/%{name}/lib/autolink-0.10.1.jar
%{_datadir}/%{name}/lib/aws-core-2.29.39.jar
%{_datadir}/%{name}/lib/aws-query-protocol-2.29.39.jar
%{_datadir}/%{name}/lib/aws-xml-protocol-2.29.39.jar
%{_datadir}/%{name}/lib/bcpg-jdk18on-1.79.jar
%{_datadir}/%{name}/lib/bcpkix-jdk18on-1.79.jar
%{_datadir}/%{name}/lib/bcprov-jdk18on-1.79.jar
%{_datadir}/%{name}/lib/bcutil-jdk18on-1.79.jar
%{_datadir}/%{name}/lib/checksums-2.29.39.jar
%{_datadir}/%{name}/lib/checksums-spi-2.29.39.jar
%{_datadir}/%{name}/lib/classmate-1.7.0.jar
%{_datadir}/%{name}/lib/commonmark-0.21.0.jar
%{_datadir}/%{name}/lib/commonmark-ext-autolink-0.21.0.jar
%{_datadir}/%{name}/lib/commons-codec-1.17.1.jar
%{_datadir}/%{name}/lib/commons-compress-1.27.1.jar
%{_datadir}/%{name}/lib/commons-io-2.18.0.jar
%{_datadir}/%{name}/lib/commons-jexl3-3.4.0.jar
%{_datadir}/%{name}/lib/commons-lang3-3.17.0.jar
%{_datadir}/%{name}/lib/commons-net-3.11.1.jar
%{_datadir}/%{name}/lib/commons-text-1.13.0.jar
%{_datadir}/%{name}/lib/compiler-0.9.14.jar
%{_datadir}/%{name}/lib/crt-core-2.29.39.jar
%{_datadir}/%{name}/lib/eddsa-0.3.0.jar
%{_datadir}/%{name}/lib/endpoints-spi-2.29.39.jar
%{_datadir}/%{name}/lib/eventstream-1.0.1.jar
%{_datadir}/%{name}/lib/failsafe-3.3.2.jar
%{_datadir}/%{name}/lib/feign-core-13.5.jar
%{_datadir}/%{name}/lib/feign-form-3.8.0.jar
%{_datadir}/%{name}/lib/feign-httpclient-13.5.jar
%{_datadir}/%{name}/lib/feign-jackson-13.5.jar
%{_datadir}/%{name}/lib/http-auth-2.29.39.jar
%{_datadir}/%{name}/lib/http-auth-aws-2.29.39.jar
%{_datadir}/%{name}/lib/http-auth-aws-eventstream-2.29.39.jar
%{_datadir}/%{name}/lib/http-auth-spi-2.29.39.jar
%{_datadir}/%{name}/lib/http-client-spi-2.29.39.jar
%{_datadir}/%{name}/lib/httpclient-4.5.14.jar
%{_datadir}/%{name}/lib/httpcore-4.4.16.jar
%{_datadir}/%{name}/lib/identity-spi-2.29.39.jar
%{_datadir}/%{name}/lib/jackson-annotations-2.18.2.jar
%{_datadir}/%{name}/lib/jackson-core-2.18.2.jar
%{_datadir}/%{name}/lib/jackson-databind-2.18.2.jar
%{_datadir}/%{name}/lib/jackson-dataformat-toml-2.18.2.jar
%{_datadir}/%{name}/lib/jackson-dataformat-xml-2.18.2.jar
%{_datadir}/%{name}/lib/jackson-dataformat-yaml-2.18.2.jar
%{_datadir}/%{name}/lib/jackson-datatype-jsr310-2.18.2.jar
%{_datadir}/%{name}/lib/jakarta.activation-2.0.1.jar
%{_datadir}/%{name}/lib/jakarta.mail-2.0.1.jar
%{_datadir}/%{name}/lib/jcl-over-slf4j-2.0.16.jar
%{_datadir}/%{name}/lib/jreleaser-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-artifactory-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-azure-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-bluesky-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-codeberg-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-command-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-config-json-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-config-toml-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-config-yaml-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-discord-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-discourse-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-engine-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-ftp-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-genericgit-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-git-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-gitea-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-github-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-gitlab-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-gitter-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-google-chat-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-http-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-java-sdk-commons-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-linkedin-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-logger-api-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-mastodon-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-mattermost-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-mavencentral-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-model-api-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-model-impl-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-nexus2-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-opencollective-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-resource-bundle-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-s3-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-sdkman-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-signing-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-slack-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-smtp-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-ssh-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-teams-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-telegram-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-templates-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-tool-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-twitter-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-utils-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-webhooks-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/jreleaser-zulip-java-sdk-1.16.0.jar
%{_datadir}/%{name}/lib/json-utils-2.29.39.jar
%{_datadir}/%{name}/lib/jsonschema-generator-4.36.0.jar
%{_datadir}/%{name}/lib/jsonschema-module-jackson-4.36.0.jar
%{_datadir}/%{name}/lib/metrics-spi-2.29.39.jar
%{_datadir}/%{name}/lib/org.eclipse.jgit-5.13.3.202401111512-r.jar
%{_datadir}/%{name}/lib/picocli-4.7.6.jar
%{_datadir}/%{name}/lib/profiles-2.29.39.jar
%{_datadir}/%{name}/lib/protocol-core-2.29.39.jar
%{_datadir}/%{name}/lib/reactive-streams-1.0.4.jar
%{_datadir}/%{name}/lib/regions-2.29.39.jar
%{_datadir}/%{name}/lib/retries-2.29.39.jar
%{_datadir}/%{name}/lib/retries-spi-2.29.39.jar
%{_datadir}/%{name}/lib/s3-2.29.39.jar
%{_datadir}/%{name}/lib/sdk-core-2.29.39.jar
%{_datadir}/%{name}/lib/slf4j-api-2.0.16.jar
%{_datadir}/%{name}/lib/slf4j-simple-2.0.16.jar
%{_datadir}/%{name}/lib/snakeyaml-2.3.jar
%{_datadir}/%{name}/lib/sshj-0.39.0.jar
%{_datadir}/%{name}/lib/stax2-api-4.2.2.jar
%{_datadir}/%{name}/lib/third-party-jackson-core-2.29.39.jar
%{_datadir}/%{name}/lib/tika-core-2.9.2.jar
%{_datadir}/%{name}/lib/twitter4j-core-4.1.2.jar
%{_datadir}/%{name}/lib/utils-2.29.39.jar
%{_datadir}/%{name}/lib/woodstox-core-7.1.0.jar
%{_datadir}/%{name}/lib/xz-1.10.jar
%{_datadir}/%{name}/lib/yamllint-1.6.1.jar
%{_datadir}/%{name}/lib/zstd-jni-1.5.6-8.jar
%{_datadir}/%{name}/licenses/LICENSE-BSD-2-Clause
%{_datadir}/%{name}/licenses/LICENSE-BSD-2-Clause-FreeBSD
%{_datadir}/%{name}/licenses/LICENSE-Bouncy-Castle
%{_datadir}/%{name}/licenses/LICENSE-CC0
%{_datadir}/%{name}/licenses/LICENSE-EDL-1.0
%{_datadir}/%{name}/licenses/LICENSE-MIT
%{_datadir}/%{name}/licenses/LICENSE-jzlib
